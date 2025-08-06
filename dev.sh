#!/bin/bash
# dev.sh - Helper script for SapphireUI UI development
# Usage:
#   ./dev.sh components sidebars cards
#   ./dev.sh charts line bar
#   ./dev.sh pro table
#   ./dev.sh mixed sidebars cards line pie table
#   ./dev.sh list components|charts|pro|all

# Function to list available components
list_components() {
  echo "Available components:"
  # List directories in pantry, excluding __pycache__ and other Python artifacts
  find SapphireUI/pantry/ -maxdepth 1 -type d | grep -v "__pycache__" | grep -v "/__" | sed 's/SapphireUI\/pantry\///' | grep -v "^$" | sed 's/^\///' | sort
}

# Function to list available charts
list_charts() {
  echo "Available charts:"
  # List directories in charts, excluding __pycache__ and other Python artifacts
  find SapphireUI/charts/ -maxdepth 1 -type d | grep -v "__pycache__" | grep -v "/__" | sed 's/SapphireUI\/charts\///' | grep -v "^$" | sed 's/^\///' | sort
}

# Function to list available pro components
list_pro() {
  echo "Available pro components:"
  # List directories in pro, excluding __pycache__ and other Python artifacts
  find SapphireUI/pro/ -maxdepth 1 -type d | grep -v "__pycache__" | grep -v "/__" | sed 's/SapphireUI\/pro\///' | grep -v "^$" | sed 's/^\///' | sort
}


MODE=$1
shift

case $MODE in
  list)
      TYPE=$1
      case $TYPE in
        components)
          list_components
          ;;
        charts)
          list_charts
          ;;
        pro)
          list_pro
          ;;
        all)
          list_components
          echo ""
          list_charts
          echo ""
          list_pro
          ;;
        *)
          echo "Available categories to list: components, charts, pro, all"
          ;;
      esac
      exit 0
      ;;
  pro)
    export SAPPHIREUI_DEV_MODE=true
    export SAPPHIREUI_PRO=$(echo $@ | tr ' ' ',')
    unset SAPPHIREUI_COMPONENTS
    unset SAPPHIREUI_CHARTS
    echo "Development mode: Pro components only - ${SAPPHIREUI_PRO}"
    ;;
  components)
    export SAPPHIREUI_DEV_MODE=true
    export SAPPHIREUI_COMPONENTS=$(echo $@ | tr ' ' ',')
    unset SAPPHIREUI_CHARTS
    unset SAPPHIREUI_PRO
    echo "Development mode: Components only - ${SAPPHIREUI_COMPONENTS}"
    ;;
  charts)
    export SAPPHIREUI_DEV_MODE=true
    export SAPPHIREUI_CHARTS=$(echo $@ | tr ' ' ',')
    unset SAPPHIREUI_COMPONENTS
    unset SAPPHIREUI_PRO
    echo "Development mode: Charts only - ${SAPPHIREUI_CHARTS}"
    ;;
  mixed)
    export SAPPHIREUI_DEV_MODE=true

    SELECTED_COMPONENTS=""
    SELECTED_CHARTS=""
    SELECTED_PRO=""

    for item in "$@"; do
      if [ -d "SapphireUI/pantry/$item" ]; then
        if [ -z "$SELECTED_COMPONENTS" ]; then
          SELECTED_COMPONENTS="$item"
        else
          SELECTED_COMPONENTS="$SELECTED_COMPONENTS,$item"
        fi
      elif [ -d "SapphireUI/charts/$item" ]; then
        if [ -z "$SELECTED_CHARTS" ]; then
          SELECTED_CHARTS="$item"
        else
          SELECTED_CHARTS="$SELECTED_CHARTS,$item"
        fi
      elif [ -d "SapphireUI/pro/$item" ]; then
        if [ -z "$SELECTED_PRO" ]; then
          SELECTED_PRO="$item"
        else
          SELECTED_PRO="$SELECTED_PRO,$item"
        fi
      else
        echo "Warning: '$item' not found as a component, chart, or pro component"
      fi
    done

    export SAPPHIREUI_COMPONENTS="$SELECTED_COMPONENTS"
    export SAPPHIREUI_CHARTS="$SELECTED_CHARTS"
    export SAPPHIREUI_PRO="$SELECTED_PRO"

    echo "Development mode: Mixed selection"
    [ ! -z "$SELECTED_COMPONENTS" ] && echo "  Components: $SELECTED_COMPONENTS"
    [ ! -z "$SELECTED_CHARTS" ] && echo "  Charts: $SELECTED_CHARTS"
    [ ! -z "$SELECTED_PRO" ] && echo "  Pro: $SELECTED_PRO"
    ;;
  off)
    unset SAPPHIREUI_DEV_MODE
    unset SAPPHIREUI_COMPONENTS
    unset SAPPHIREUI_CHARTS
    unset SAPPHIREUI_PRO
    echo "Development mode: Disabled (loading all components)"
    ;;
  *)
    echo "Invalid mode. Use: pro, components, charts, both, or off"
    exit 1
    ;;
esac

# Run Reflex
reflex run