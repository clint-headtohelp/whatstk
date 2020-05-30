"""Utils for library plots."""


import seaborn as sns


def hex_color_palette(n_colors):
    """Get palette of `n_colors` color hexadecimal codes.

    Args:
        n_colors (int): Size of the color palette.

    """
    rgb = sns.color_palette(palette="husl", n_colors=n_colors)
    color_codes = ["#"+"".join("%02X" % int(round(i*255)) for i in r) for r in rgb]
    return color_codes
