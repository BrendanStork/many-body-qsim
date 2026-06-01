import matplotlib.pyplot as plt
import numpy as np
#from .circuit import Quantum_Circuit
#from .evolution import trotter_evolve, exact_evolve
#from .expectation_values import expectation_vals_vs_time, expectation_vals_vs_trotter_steps
    
def plot_observable(
    x,
    y,
    *,
    ax=None,
    label=None,
    xlabel=None,
    ylabel=None,
    title=None,
    xlabel_fontsize=14,
    ylabel_fontsize=14,
    title_fontsize=15,
    xlim=None,
    ylim=None,
    **plot_kwargs
):
    
    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(x, y, label=label, **plot_kwargs)

    if xlabel:
        ax.set_xlabel(xlabel, fontsize=xlabel_fontsize)

    if ylabel:
        ax.set_ylabel(ylabel, fontsize=ylabel_fontsize)

    if title:
        ax.set_title(title, fontsize=title_fontsize)

    if label:
        ax.legend()
        
    #if xlim:
    #    ax.set_xlim(xlim)

    if ylim:
        ax.set_ylim(ylim)
        
    ax.set_xlim(x[0], x[-1])

    return ax

def plot_correlation_map(
    corr_map,
    *,
    ax=None,
    title=None,
    cmap='coolwarm',
    colorbar=True
):

    if ax is None:
        fig, ax = plt.subplots()

    im = ax.imshow(
        corr_map,
        cmap=cmap,
        origin='lower'
    )

    ax.set_xlabel('Site j')
    ax.set_ylabel('Site i')

    if title:
        ax.set_title(title)

    if colorbar:
        plt.colorbar(im, ax=ax)

    plt.xticks(np.arange(0, len(corr_map[0, :]), dtype=np.int32))
    plt.yticks(np.arange(0, len(corr_map[:, 0]), dtype=np.int32))

    return ax
