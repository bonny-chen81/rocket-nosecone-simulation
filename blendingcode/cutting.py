import open3d as o3d
import numpy as np

# 讀取 STL 模型
stl = o3d.io.read_triangle_mesh("aligned_swift_3d.stl")

if stl.is_empty():
    print("STL 檔案讀取失敗！")
    exit()

# 計算 AABB (Axis-Aligned Bounding Box)
aabb = stl.get_axis_aligned_bounding_box()
aabb.color = (1, 0, 0)  # 設定邊界框顏色為紅色

# 打印 AABB 範圍 (確認整體尺寸)
print("AABB 最小值:", aabb.min_bound)
print("AABB 最大值:", aabb.max_bound)

# 設定頭部的範圍 (根據 AABB 來微調)
min_bound = np.array([aabb.min_bound[0]+0.13, aabb.min_bound[1], aabb.min_bound[2] ])
max_bound = np.array([aabb.max_bound[0], aabb.max_bound[1] , aabb.max_bound[2]])

# 創建頭部的 AABB
head_box = o3d.geometry.AxisAlignedBoundingBox(min_bound, max_bound)
head_box.color = (0, 1, 0)  # 設定頭部範圍為綠色

# 使用 crop() 來裁切頭部
head_part = stl.crop(head_box)

# 確保裁切後的結果不是空的
if head_part.is_empty():
    print("頭部裁切失敗，請檢查範圍設定！")
    exit()

# 平滑化處理
head_part = head_part.filter_smooth_laplacian(number_of_iterations=10)
head_part.compute_vertex_normals()

# 顯示裁切後的頭部
o3d.visualization.draw_geometries([head_part, head_box], window_name="老鷹頭部")

o3d.io.write_triangle_mesh("swiftdone_3d.stl", head_part)
print("保存成功")
