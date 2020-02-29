import folium
from folium.plugins import MarkerCluster
import pandas as pd


def main():
    boulder_coords = [40.015, -105.2705]
    my_map = folium.Map(location=boulder_coords, zoom_start=13, tiles='CartoDB positron')
    # Define the coordinates we want our markers to be at
    CU_Boulder_coords = [40.007153, -105.266930]
    East_Campus_coords = [40.013501, -105.251889]
    SEEC_coords = [40.009837, -105.241905]

    # Add markers to the map
    folium.Marker(CU_Boulder_coords, popup='CU Boulder').add_to(my_map)
    folium.Marker(East_Campus_coords, popup='East Campus').add_to(my_map)
    folium.Marker(SEEC_coords, popup='SEEC Building').add_to(my_map)

    folium.Marker(
        location=[45.3300, -121.6823],
        popup='Some Other Location',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(my_map)

    folium.Circle(
        radius=100,
        location=[45.5244, -122.6699],
        popup='The Waterfront',
        color='crimson',
        fill=False,
    ).add_to(my_map)

    folium.CircleMarker(
        location=[45.5215, -122.6261],
        radius=50,
        popup='Laurelhurst Park',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(my_map)

    # Display the map
    my_map.save('test.html')


if __name__ == '__main__':
    main()