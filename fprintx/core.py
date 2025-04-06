# fprintx/core.py

def printx(*args, widths=None, alignments=None, styles=None, truncate=False, return_as_str=False):
    # Default values if widths, alignments, or styles are not provided
    min_arg_width = [min(len(str(arg)) for arg in args)][0]
    if widths is None:
        widths = [max(len(str(arg)) for arg in args)] * len(args)
    
    if alignments is None:
        alignments = ['<'] * len(args)
    
    if styles is None:
        styles = [''] * len(args)



    # Ensure lengths match or apply last option to remaining values
    widths = widths + ( [widths[-1]] * (max(0, len(args) - len(widths))))
    alignments = alignments + ( [alignments[-1]] * (max(0, len(args) - len(alignments))))
    styles = styles + ( [styles[-1]] * (max(0, len(args) - len(styles))))

    # print(widths, alignments, styles, min_arg_width)

    formatted_args = []
    
    for i, arg in enumerate(args):
            
        value = str(arg)
        style = styles[i]
        width = widths[i]
        alignment = alignments[i]

        if truncate and len(value) > width + 10:
            value = value[:width] + '...'
        elif truncate and len(value) > width:
            value = value[:width]



        # Apply style formatting (bold, underline, etc.)
        if style == 'bold':
            value = f"\033[1m{value}\033[0m"  + (" " * (width - 1))
        elif style == 'underline':
            value = f"\033[4m{value}\033[0m"  + (" " * (width - 1))
        elif style == 'italic':
            value = f"\033[3m{value}\033[0m" + (" " * (width - 1))
        

        # Apply alignment and width
        formatted_value = f"{value:{alignment}{width}}"
        formatted_args.append(formatted_value)
    
    # Print the formatted output
    result = " ".join(formatted_args)
    if return_as_str:
        return result
    print(result)




# printx("HEllo", 'Kow', 353434353434353434353434353434353434353434353434353434, widths=[10], styles=['', 'italic'], truncate=True)
# printx("HEllo", 'Kow', 353434353434353434353434353434353434353434353434353434, widths=[10], styles=['', 'italic'], truncate=True)
# printx("HEllo", 'Kow', 2, widths=[10], styles=['', 'italic'], truncate=True)
# printx("HEllo", 'Kow', 'lkl', widths=[10], truncate=True, styles=['bold'])


# for i in range(3):
#     printx("i:", i, "i*10:", i*10, "i^2:", i**2, widths=[3, 4, 6, 5, 4])

# print()
# for i in range(3):
#     print("i:", i, "i*10:", i*10, "i^2:", i**2)