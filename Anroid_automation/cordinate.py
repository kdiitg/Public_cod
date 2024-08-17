import matplotlib.pyplot as plt
import matplotlib.patches as patches
import re


def on_click(event):
    """Print coordinates of the click event."""
    if event.inaxes:
        print(f'Clicked at: x={event.xdata:.2f}, y={event.ydata:.2f}')



def parse_coordinates(text):
    """Parse coordinates from a text input."""
    pattern = re.compile(r'\[(\d+),(\d+)\]\s*\[\s*(\d+),(\d+)\]')
    match = pattern.match(text)
    if match:
        x1, y1, x2, y2 = map(int, match.groups())
        return (x1, y1, x2, y2)
    else:
        raise ValueError("Invalid coordinate format. Please use [x1,y1][x2,y2].")

def draw_rectangle(x1, y1, x2, y2):
    """Draw a rectangle on a plot given the coordinates."""
    fig, ax = plt.subplots()

    # Calculate width and height based on the coordinates
    width = x2 - x1
    height = y2 - y1
    
    # Create a rectangle patch with (x1, y1) as top-left and (x2, y2) as bottom-right
    rect = patches.Rectangle((x1, y1), width, height, linewidth=1, edgecolor='r', facecolor='lightblue')
    ax.add_patch(rect)

    # Set the limits of the plot
    ax.set_xlim(x1 - 10, x2 + 10)
    ax.set_ylim(y2 + 10, y1 - 10)  # Inverted y-axis to match typical coordinate system

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # ax.set_title('Rectangle Based on Coordinates')
    ax.set_title(input_text)
    
    # Keep the grid
    ax.grid(True)
    # Connect the click event to the handler
    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()

if __name__ == "__main__":
    # Get user input
    input_text = input("Enter coordinates in the format [x1,y1][x2,y2]: ")
    try:
        # Parse coordinates
        x1, y1, x2, y2 = parse_coordinates(input_text)
        # Draw rectangle
        draw_rectangle(x1, y1, x2, y2)
    except ValueError as e:
        print(e)


