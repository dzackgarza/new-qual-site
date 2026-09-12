---
schema: qual/card@1
id: P-JAEYU
kind: problem
title: The topologist's sine curve is connected but not path-connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
---

::: problem
- Show that the topologist's sine curve is connected but not path-connected.
:::

::: {.solution}
<1>1. Let
$$G=\{(x,\sin(1/x)):0<x\le1\},\qquad T=G\cup(\{0\}\times[-1,1]).$$
The set $T$ is connected.
::: {.proof}
The interval $(0,1]$ is connected, so its continuous image $G$ is connected. Its closure is exactly $T$, and the closure of a connected subset is connected.
:::

<1>2. There is no path in $T$ from the vertical segment $\{0\}\times[-1,1]$ to $G$.
::: {.proof}
Suppose $\gamma(t)=(x(t),y(t))$ were such a path, with $x(0)=0$ and $x(1)>0$. Let
$$t_0=\sup\{t\in[0,1]:x(t)=0\}.$$
Then $t_0<1$, $x(t_0)=0$, and $x(t)>0$ for $t>t_0$. For any $t_1>t_0$, continuity of $x$ implies its image on $[t_0,t_1]$ contains every value between $0$ and $x(t_1)$. Hence for all sufficiently large $n$ there are times tending to $t_0$ at which
$$x=\frac1{\pi/2+2\pi n}\quad\text{and}\quad x=\frac1{3\pi/2+2\pi n}.$$
At these times $y=1$ and $y=-1$, respectively. The times must tend to $t_0$: on every compact interval $[t_0+\delta,t_1]$, the positive continuous function $x$ has a positive minimum. Thus $y(t)$ cannot converge to the single value $y(t_0)$, contradicting continuity of $\gamma$.
:::

<1>3. Therefore the topologist's sine curve is connected but not path-connected.
::: {.proof}
Use <1>1 and <1>2.
:::
:::
