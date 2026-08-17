---
schema: qual/card@1
id: E-3QAC4
kind: exercise
title: "f and fbar holomorphic implies constant"
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-riemann
  - holomorphic-functions
relations: []
review: draft
solved: true
---
:::{.exercise title="f and fbar holomorphic implies constant"}
Show that if $f$ and $\bar{f}$ are both holomorphic on a domain $\Omega$, then $f$ is constant on $\Omega$.

:::

:::{.solution}
\envlist

- Strategy: show $f'=0$.
- Write $f = u + iv$. 
  Since $f$ is analytic, it satisfies CR, so 
  \[
  u_x = v_y && u_y = -v_x
  .\]

- Similarly write $\bar f = U + iV$ where $U = u$ and $V = -v$.
  Since $\bar f$ is analytic, it also satisfies CR , so
\[
U_x = V_y && U_y = -V_x \\ \\
\implies u_x = -v_y && u_y = v_x
.\]

- Add the LHS of these two equations to get $2u_x = 0 \implies u_x = 0$.
  Subtract the right-hand side to get $-2v_x = 0 \implies v_x = 0$

- Since $f$ is analytic, it is holomorphic, so $f'$ exists and satisfies $f' = u_x + iv_x$.
  But by above, this is zero.
- By the previous exercise, $f'=0 \implies f$ is constant.
:::
