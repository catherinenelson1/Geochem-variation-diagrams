# Creates major element variation diagrams (Harker plots)
# 1 file per dataset.


def makeHarker(fileList, elementsList, datasetNames, outputFileName):

    # Import required modules
    import pandas as pd
    import matplotlib.pyplot as plt

    datasetsDict = {}

    # Import data files, convert elements to list
    for i, f in enumerate(fileList):
        d = pd.read_csv(f, index_col=0)
        dataName = datasetNames[i]

        for e in elementsList:
            datasetsDict[(dataName, e)] = d[e].tolist()

    # Change font
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 8

    # Set up 2x3 plots
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
    sub = [ax1, ax2, ax3, ax4, ax5, ax6]

    labels = [r'SiO$_2$ (wt%)', r'FeO$_T$ (wt%)', r'Al$_2$O$_3$ (wt%)', 'CaO (wt%)', r'TiO$_2$ (wt%)',
              r'P$_2$O$_5$ (wt%)']
    symbolsDict = {'Vaigat': '^', 'Maligat': 'v', 'Kanisut': 'p', 'Hareoen': 'D', 'Delta': 'o'}
    coloursDict = {'Vaigat': '#7fc97f', 'Maligat': '#beaed4', 'Kanisut': '#fdc086',
                   'Hareoen': '#386cb0', 'Delta': '#f0027f'}
    titles = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)']

    # Make each plot, add labels, etc.
    for s, e in enumerate(elements[1:]):
        for n in datasetNames:
            sub[s].plot(datasetsDict[n, 'MgO'], datasetsDict[n, e], symbolsDict[n], markerfacecolor=coloursDict[n],
                        markeredgecolor=coloursDict[n], markersize=4, label=n)

        sub[s].set_xlabel('MgO (wt%)')
        sub[s].set_ylabel(labels[s])
        sub[s].legend(numpoints=1, fontsize=6)
        sub[s].set_title(titles[s], x=-0.1, y=1.05)

    plt.tight_layout()

    # Save file
    fig.set_size_inches(6, 8)
    name = outputFileName + '.png'
    plt.savefig(name, dpi=300, bbox_inches='tight', pad_inches=0.25)


files = ['Vaigat.csv', 'Maligat.csv', 'Kanisut.csv', 'Hareoen.csv', 'Delta XRF.csv']
elements = ['MgO', 'SiO2', 'FeOt', 'Al2O3', 'CaO', 'TiO2', 'P2O5']
data = ['Vaigat', 'Maligat', 'Kanisut', 'Hareoen', 'Delta']
makeHarker(files, elements, data, 'Figure 12')
