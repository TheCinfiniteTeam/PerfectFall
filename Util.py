#-*-coding:UTF-8 -*-
# 常用函数集合


def gradient_color(color_list, color_sum=700):
    """ 给定颜色List，输出渐变色 """
    color_center_count = len(color_list)
    color_sub_count = int(color_sum / (color_center_count - 1))
    color_index_start = 0
    color_map = []
    for color_index_end in range(1, color_center_count):
        color_rgb_start = color_list[color_index_start]
        color_rgb_end = color_list[color_index_end]
        r_step = (color_rgb_end[0] - color_rgb_start[0]) / color_sub_count
        g_step = (color_rgb_end[1] - color_rgb_start[1]) / color_sub_count
        b_step = (color_rgb_end[2] - color_rgb_start[2]) / color_sub_count
        # 生成中间渐变色
        now_color = color_rgb_start
        color_map.append(now_color)
        for color_index in range(1, color_sub_count):
            now_color = [now_color[0] + r_step, now_color[1] + g_step, now_color[2] + b_step]
            color_map.append(now_color)
        color_index_start = color_index_end
    return color_map
