---
schema: qual/card@1
id: P-JZXST
kind: problem
title: The torus as a double cover of the Klein bottle
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Cell Complexes
relations: []
review: draft
---

::: problem
3. Draw CW square for $T$ and cut down the center to see two copies of $K$.
:::

::: {.solution}
<1>1. Model the Klein bottle as
$$K=[0,1]\times[0,1]/(0,y)\sim(1,y),\quad (x,0)\sim(1-x,1).$$
::: {.proof}
This is the standard square model with one pair of opposite sides glued in the same direction and the other pair in opposite directions.
:::

<1>2. Take two copies of this square side-by-side. After gluing the vertical sides between the two copies, the remaining outer vertical sides are identified in the same direction, while the top and bottom identifications become untwisted across the doubled rectangle.
::: {.proof}
Traversing the twisted identification twice reverses orientation twice, hence gives the identity on the transverse interval.
:::

<1>3. The doubled rectangle therefore has the usual torus edge identifications, and the map collapsing the two copies to the original square is a $2$-sheeted covering
$$\boxed{T^2\to K.}$$
::: {.proof}
Away from the quotient edges this is visibly two-to-one, and the edge identifications are compatible with the local product neighborhoods, so it is a covering map.
:::
:::
