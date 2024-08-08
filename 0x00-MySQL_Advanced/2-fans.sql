-- a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
-- Column names must be: origin and nb_fans
SELECT origin, COUNT(*) AS nb_fans
from metal_bands
GROUP BY Origin
ORDER BY nb_fans DESC;
