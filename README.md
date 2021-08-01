# vizathon2021

## Instructions

- (Optionally) Build the docker image
- Download the 'Most Recent Institution Level Data' data from the [College Scorecard](https://data.ed.gov/dataset/college-scorecard-all-data-files-through-6-2020/) and rename it to **collegedata170m.csv**
- Run python clean.py
- Run streamlit run vization.py

## How to use

![image](https://github.com/julianweng/collegeviz/blob/master/readmeimages/columnselect.png?raw=true)

At the top, users can select which information they want to display about a college. By default, common statistics such as the name of the college, ZIP, Admission rate, and mean earnings 10 years after entrance are displayed, but the user can add more easily.

![image](https://github.com/julianweng/collegeviz/blob/master/readmeimages/sidebar.png?raw=true)

In the sidebar, users can use filters to select specific colleges with certain atributes to display in the graph below. For instance, if one wanted to only display selective schools, one can select admission rate in the *Filter One* dropdown menu and lower the range to something like 0.0-0.5 or so.

Here, the user can also select whichever variable the user wants in the x and y axices for the graph.

![image](https://github.com/julianweng/collegeviz/blob/master/readmeimages/chart.png?raw=true)

On the chart itself, one can click on the different colored categories to select specific categories to display. In this example, the colors represent different kinds of colleges, and it is set up to only display selective public, ivy plus, and other elite schools. One can also hover over each college/data point for more information, zoom in to full screen, and save the chart as a PNG.


## Data Sources
- https://data.ed.gov/dataset/college-scorecard-all-data-files-through-6-2020/
- https://opportunityinsights.org/data/
