This project will show basic info about wildfires in California.
It uses data from fire.ca.gov

Example:
+----------------------+-----------------+---------------+--------------+--------------------------+----------------------+
|      Fire Name       | Size (in acres) | Containment % | Date Started |           City           |        County        |
+----------------------+-----------------+---------------+--------------+--------------------------+----------------------+
|    Palisades Fire    |     23713.0     |      61.0     |  2025-01-07  |    Pacific Palisades     |     Los Angeles      |
|      Eaton Fire      |     14021.0     |      87.0     |  2025-01-07  |    Altadena/Pasadena     |     Los Angeles      |
|     Kenneth Fire     |      1052.0     |     100.0     |  2025-01-09  |        West Hills        | Los Angeles, Ventura |
|      Hurst Fire      |      799.0      |     100.0     |  2025-01-07  |          Sylmar          |     Los Angeles      |
|      Lidia Fire      |      395.0      |     100.0     |  2025-01-08  |          Acton           |     Los Angeles      |
|      Auto Fire       |       61.0      |     100.0     |  2025-01-13  |         Ventura          |       Ventura        |
|     Sunset Fire      |       42.8      |     100.0     |  2025-01-08  |     Hollywood Hills      |     Los Angeles      |
|       Oak Fire       |       42.0      |     100.0     |  2025-01-01  |       Santa Maria        |    Santa Barbara     |
| Little Mountain Fire |       34.0      |     100.0     |  2025-01-15  |      San Bernardino      |    San Bernardino    |
|     Woodley Fire     |       30.0      |     100.0     |  2025-01-08  |     Sepulveda Basin      |     Los Angeles      |
|     Border Fire      |       25.0      |     100.0     |  2025-01-01  | Otay Mountain Wilderness |      San Diego       |
|     Archer Fire      |       19.0      |     100.0     |  2025-01-10  |      Granada Hills       |     Los Angeles      |
|      Tyler Fire      |       11.0      |     100.0     |  2025-01-08  |        Coachella         |      Riverside       |
|     Olivas Fire      |       11.0      |     100.0     |  2025-01-08  |         Ventura          |       Ventura        |
|      Scout Fire      |       2.0       |     100.0     |  2025-01-14  |        Riverside         |      Riverside       |
+----------------------+-----------------+---------------+--------------+--------------------------+----------------------+

It will prompt if you want to include active fires in the table and by what column you would like to sort by.

Python Dependencies:
PrettyTable
Requests