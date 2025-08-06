#!/bin/bash

# Dynamic Multi-Level Application Launcher with Rofi
# Author: Assistant
# Description: Navigate through categorized tools using keyboard-only interface

# Configuration
LAUNCHER_DIR="$HOME/echo-launcher"
ROFI_THEME="dmenu"  # Change this to your preferred rofi theme
BACK_OPTION="⬅️ Back"
SEPARATOR=" / "

# Create launcher directory if it doesn't exist
mkdir -p "$LAUNCHER_DIR"

# Function to create breadcrumb from current path
create_breadcrumb() {
    local current_path="$1"
    local base_path="$LAUNCHER_DIR"
    
    # Remove base path and leading slash
    local relative_path="${current_path#$base_path}"
    relative_path="${relative_path#/}"
    
    if [ -z "$relative_path" ]; then
        echo "🚀 Echo Launcher"
    else
        # Replace / with separator and add root
        echo "🚀 Echo Launcher${SEPARATOR}${relative_path//\//$SEPARATOR}"
    fi
}

# Function to get display name with icons
get_display_name() {
    local item="$1"
    local full_path="$2"
    
    if [ -d "$full_path" ]; then
        # Directory - add folder icon
        echo "📁 $item"
    else
        # File - add application icon
        echo "⚡ $item"
    fi
}

# Function to escape special characters for rofi
escape_for_rofi() {
    echo "$1" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g'
}

# Function to show directory contents
show_directory() {
    local current_dir="$1"
    local options=()
    local display_options=()
    
    # Add back option if not in root directory
    if [ "$current_dir" != "$LAUNCHER_DIR" ]; then
        options+=("$BACK_OPTION")
        display_options+=("$BACK_OPTION")
    fi
    
    # Read directory contents
    if [ -d "$current_dir" ]; then
        while IFS= read -r -d '' item; do
            local basename_item=$(basename "$item")
            local display_name=$(get_display_name "$basename_item" "$item")
            
            options+=("$basename_item")
            display_options+=("$display_name")
        done < <(find "$current_dir" -maxdepth 1 -mindepth 1 -print0 | sort -z)
    fi
    
    # If no items found, show empty message
    if [ ${#options[@]} -eq 0 ] || ([ ${#options[@]} -eq 1 ] && [ "${options[0]}" = "$BACK_OPTION" ]); then
        if [ "$current_dir" != "$LAUNCHER_DIR" ]; then
            display_options+=("📭 Empty directory")
            options+=("EMPTY")
        else
            display_options+=("📭 No categories found")
            display_options+=("💡 Create directories in $LAUNCHER_DIR")
            options+=("EMPTY")
            options+=("HELP")
        fi
    fi
    
    # Create breadcrumb
    local breadcrumb=$(create_breadcrumb "$current_dir")
    
    # Show rofi menu
    local selected_display
    printf '%s\n' "${display_options[@]}" | rofi -dmenu \
        -i \
        -p "$breadcrumb" \
        -theme "$ROFI_THEME" \
        -format 'i' \
        -selected-row 0 > /tmp/rofi_selection_index 2>/dev/null
    
    local selection_index
    selection_index=$(cat /tmp/rofi_selection_index 2>/dev/null)
    rm -f /tmp/rofi_selection_index
    
    # Handle selection
    if [ -n "$selection_index" ] && [ "$selection_index" -ge 0 ] && [ "$selection_index" -lt ${#options[@]} ]; then
        local selected="${options[$selection_index]}"
        handle_selection "$selected" "$current_dir"
    fi
}

# Function to handle user selection
handle_selection() {
    local selected="$1"
    local current_dir="$2"
    
    case "$selected" in
        "$BACK_OPTION")
            # Go back to parent directory
            local parent_dir=$(dirname "$current_dir")
            if [ "$parent_dir" != "/" ] && [ "$parent_dir" != "$current_dir" ]; then
                show_directory "$parent_dir"
            else
                show_directory "$LAUNCHER_DIR"
            fi
            ;;
        "EMPTY")
            # Do nothing for empty placeholder
            show_directory "$current_dir"
            ;;
        "HELP")
            # Show help message
            rofi -e "Create directories and files in $LAUNCHER_DIR to build your launcher structure.\n\nExample:\nmkdir -p '$LAUNCHER_DIR/Programming/Python'\necho 'code' > '$LAUNCHER_DIR/Programming/Python/VSCode'"
            show_directory "$current_dir"
            ;;
        *)
            local target_path="$current_dir/$selected"
            
            if [ -d "$target_path" ]; then
                # It's a directory, navigate into it
                show_directory "$target_path"
            elif [ -f "$target_path" ]; then
                # It's a file, execute the command inside it
                execute_command "$target_path" "$selected"
            else
                # Item doesn't exist (shouldn't happen)
                rofi -e "Error: '$selected' not found in '$current_dir'"
                show_directory "$current_dir"
            fi
            ;;
    esac
}

# Function to execute command from file
execute_command() {
    local file_path="$1"
    local app_name="$2"
    
    # Read command from file
    local command
    command=$(cat "$file_path" 2>/dev/null | head -n 1)
    
    if [ -z "$command" ]; then
        rofi -e "Error: No command found in '$app_name'"
        return 1
    fi
    
    # Ask for confirmation (optional)
    local confirm
    confirm=$(echo -e "Yes\nNo" | rofi -dmenu -p "Launch $app_name? Command: $command")
    
    if [ "$confirm" = "Yes" ]; then
        # Execute command in background and detach from terminal
        nohup bash -c "$command" >/dev/null 2>&1 &
        
        # Optional: show success message
        # rofi -e "Launched: $app_name"
        
        # Exit launcher after successful execution
        exit 0
    else
        # Go back to current directory
        local current_dir=$(dirname "$file_path")
        show_directory "$current_dir"
    fi
}

# Function to setup example structure
setup_example() {
    if [ ! -d "$LAUNCHER_DIR" ] || [ -z "$(ls -A "$LAUNCHER_DIR" 2>/dev/null)" ]; then
        echo "Setting up example launcher structure..."
        
        # Programming category
        mkdir -p "$LAUNCHER_DIR/Programming/Python/Tools"
        mkdir -p "$LAUNCHER_DIR/Programming/Web"
        
        echo "code" > "$LAUNCHER_DIR/Programming/Python/Tools/VSCode"
        echo "pycharm" > "$LAUNCHER_DIR/Programming/Python/Tools/PyCharm"
        echo "python3" > "$LAUNCHER_DIR/Programming/Python/Python REPL"
        echo "firefox" > "$LAUNCHER_DIR/Programming/Web/Firefox"
        echo "google-chrome" > "$LAUNCHER_DIR/Programming/Web/Chrome"
        
        # Security category
        mkdir -p "$LAUNCHER_DIR/Security/Network/Scanning"
        mkdir -p "$LAUNCHER_DIR/Security/Exploitation/Android"
        
        echo "nmap" > "$LAUNCHER_DIR/Security/Network/Scanning/Nmap"
        echo "wireshark" > "$LAUNCHER_DIR/Security/Network/Wireshark"
        echo "metasploit-framework" > "$LAUNCHER_DIR/Security/Exploitation/Metasploit"
        echo "java -jar androrat.jar" > "$LAUNCHER_DIR/Security/Exploitation/Android/AndroRAT"
        echo "java -jar droidjack.jar" > "$LAUNCHER_DIR/Security/Exploitation/Android/DroidJack"
        
        # System category
        mkdir -p "$LAUNCHER_DIR/System/Monitoring"
        mkdir -p "$LAUNCHER_DIR/System/Files"
        
        echo "htop" > "$LAUNCHER_DIR/System/Monitoring/Htop"
        echo "iotop" > "$LAUNCHER_DIR/System/Monitoring/IOTop"
        echo "nautilus" > "$LAUNCHER_DIR/System/Files/File Manager"
        echo "gnome-terminal" > "$LAUNCHER_DIR/System/Terminal"
        
        # Media category
        mkdir -p "$LAUNCHER_DIR/Media/Video"
        mkdir -p "$LAUNCHER_DIR/Media/Audio"
        
        echo "vlc" > "$LAUNCHER_DIR/Media/Video/VLC"
        echo "mpv" > "$LAUNCHER_DIR/Media/Video/MPV"
        echo "audacity" > "$LAUNCHER_DIR/Media/Audio/Audacity"
        echo "spotify" > "$LAUNCHER_DIR/Media/Audio/Spotify"
        
        echo "Example structure created in $LAUNCHER_DIR"
    fi
}

# Main function
main() {
    # Setup example if directory is empty
    setup_example
    
    # Start from launcher directory
    show_directory "$LAUNCHER_DIR"
}

# Handle command line arguments
case "${1:-}" in
    --help|-h)
        cat << EOF
Dynamic Multi-Level Application Launcher

Usage: $0 [OPTIONS]

Options:
    --help, -h          Show this help message
    --setup-example     Setup example directory structure
    --launcher-dir DIR  Set custom launcher directory (default: $LAUNCHER_DIR)

Directory Structure:
    - Each directory represents a category
    - Each file contains a shell command to execute
    - Unlimited nesting is supported
    - Use Unicode characters and spaces freely

Example:
    mkdir -p "$LAUNCHER_DIR/Programming/Python"
    echo 'code' > "$LAUNCHER_DIR/Programming/Python/VSCode"

Navigation:
    - Arrow keys or vi keys to navigate
    - Enter to select
    - Escape to cancel
    - Select folders to dive deeper
    - Select "⬅️ Back" to go up one level

EOF
        exit 0
        ;;
    --setup-example)
        rm -rf "$LAUNCHER_DIR"
        setup_example
        echo "Example structure created. Run $0 to start launcher."
        exit 0
        ;;
    --launcher-dir)
        if [ -n "$2" ]; then
            LAUNCHER_DIR="$2"
            shift 2
        else
            echo "Error: --launcher-dir requires a directory path"
            exit 1
        fi
        ;;
    *)
        # Default behavior - start launcher
        ;;
esac

# Check if rofi is installed
if ! command -v rofi >/dev/null 2>&1; then
    echo "Error: rofi is not installed. Please install rofi first."
    echo "Ubuntu/Debian: sudo apt install rofi"
    echo "Arch Linux: sudo pacman -S rofi"
    echo "Fedora: sudo dnf install rofi"
    exit 1
fi

# Start the launcher
main "$@"
