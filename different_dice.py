import pygal

from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存贮再一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequecies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result + 1):
    frequecie = results.count(value)
    frequecies.append(frequecie)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequecies)
hist.render_to_file('die_visal.svg')