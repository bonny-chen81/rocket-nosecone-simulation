import open3d as o3d

stl = o3d.io.read_triangle_mesh("swift_3d.stl")
if stl.is_empty():
    print("STL 檔案讀取失敗！")
    exit()

obb = stl.get_oriented_bounding_box()
stl.rotate(obb.R.T, center=obb.center)
# 重新計算 AABB
aabb = stl.get_axis_aligned_bounding_box()
aabb.color = (1, 0, 0)  # 紅色

stl.compute_vertex_normals()
# 顯示結果
o3d.visualization.draw_geometries([stl, obb, aabb], window_name="旋轉對齊後的 AABB")

o3d.io.write_triangle_mesh("aligned_swift_3d.stl", stl)
print("STL 已儲存")
