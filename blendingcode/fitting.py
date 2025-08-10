import numpy as np
import trimesh


# === Revolve 成鼻錐 mesh ===
def generate_revolved_mesh(z_vals, r_vals, segments=100):
    theta = np.linspace(0, 2 * np.pi, segments)
    vertices = []

    for z, r in zip(z_vals, r_vals):
        for t in theta:
            x = r * np.cos(t)
            y = r * np.sin(t)
            vertices.append([x, y, z])

    vertices = np.array(vertices)
    faces = []
    rings = len(z_vals)
    pts_per_ring = segments

    for i in range(rings - 1):
        for j in range(pts_per_ring):
            next_j = (j + 1) % pts_per_ring
            a = i * pts_per_ring + j
            b = i * pts_per_ring + next_j
            c = (i + 1) * pts_per_ring + j
            d = (i + 1) * pts_per_ring + next_j
            faces.append([a, b, d])
            faces.append([a, d, c])

    return trimesh.Trimesh(vertices=vertices, faces=faces)

# === 載入兩個 STL 模型 ===
nose_cone = trimesh.load("BNC-20B_Nose_Cone_No_Shoulder.stl")
falcon_cone = trimesh.load("Sailfishdone_3d.stl")

# === 自動將 falcon nose cone 縮放成與 BNC 同樣 Z 軸長度 ===
z_nose_min, z_nose_max = nose_cone.bounds[:, 2]
z_falcon_min, z_falcon_max = falcon_cone.bounds[:, 2]
length_nose = z_nose_max - z_nose_min
length_falcon = z_falcon_max - z_falcon_min
scale_factor = length_nose / length_falcon
falcon_cone.apply_scale(scale_factor)

# === 重取樣為相同點數 ===
def sample_mesh_uniform(mesh, n_points=10000):
    points, _ = trimesh.sample.sample_surface_even(mesh, n_points)
    if len(points) < n_points:
        # 隨機補足不足點數（可以重複）
        additional = points[np.random.choice(len(points), n_points - len(points), replace=True)]
        points = np.vstack([points, additional])
    return points

n_samples = 10000
alpha = 0.2  # 0 = 完全鼻錐，1 = 完全老鷹
points_nose = sample_mesh_uniform(nose_cone, n_samples)
points_falcon = sample_mesh_uniform(falcon_cone, n_samples)

# === 對應點混合 ===
blended_points = (1 - alpha) * points_nose + alpha * points_falcon

# === 建立點雲，並使用凸包重建外型 ===
blended_pointcloud = trimesh.points.PointCloud(blended_points)
blended_mesh = blended_pointcloud.convex_hull

# === 匯出融合結果 ===
blended_mesh.export("Sailfishdone_3d_blended_0.2.stl")
print("融合鼻錐已輸出")