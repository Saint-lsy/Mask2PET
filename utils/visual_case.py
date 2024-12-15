import nibabel as nib
import matplotlib.pyplot as plt

# # 读取nii.gz文件
# nii_file = '/home/syliu/workspace/Mask2PET/results_new/metrics/nocrop/target_0.nii.gz'
# img = nib.load(nii_file)
# data = img.get_fdata()

# print(data.shape)  # 显示图像数据的形状
# # 显示图像数据
# plt.figure()
# plt.imshow(data[:, :, data.shape[2] // 2], cmap='gray')  # 显示中间切片
# plt.axis('off')  # 关闭坐标轴
# plt.show()
# plt.savefig('target_0.png')


import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# 读zai na取nii.gz文件
nii_file = '/home/syliu/workspace/Mask2PET/results_new/metrics/nocrop/target_0.nii.gz'
img = nib.load(nii_file)
data = img.get_fdata()

# 创建一个三维图像
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# 显示三维图像数据
threshold = 0.5  # 设置阈值
x, y, z = np.where(data > threshold)
ax.scatter(x, y, z, c=data[x, y, z], cmap='gray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
