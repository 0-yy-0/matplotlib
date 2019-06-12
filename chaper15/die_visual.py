import pygal

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存贮再一个列表中
results = [die.roll() for roll_num in range(1000)]

# 分析结果
frequecies = [results.count(value) for value in range(1, die.num_sides + 1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequecies)
hist.render_to_file('die_visal.svg')