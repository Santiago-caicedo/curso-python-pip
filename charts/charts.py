import matplotlib.pyplot as plt

def generate_píe_chart():
    labels = ['A', 'B', 'C']
    Values = [200, 43, 120]

    fig, ax = plt.subplots()
    ax.pie(Values, labels=labels)
    plt.savefig('pie.png')
    plt.close()