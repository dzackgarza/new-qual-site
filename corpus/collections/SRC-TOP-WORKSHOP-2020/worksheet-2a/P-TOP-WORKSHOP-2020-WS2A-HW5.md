---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW5
kind: problem
title: The topologist's sine curve is connected but not path connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the graph is homeomorphic to
    (0, inf) via the first coordinate, hence connected; adding a closure point to a connected set
    keeps it connected, with the standard justification (G subset X subset closure G). For
    non-path-connectedness the argument now records that x(t) > 0 for t > t_0 rather than merely
    saying so (no negative value occurs in X, and zero does not occur by the definition of t_0),
    and that the image of [t_0, t_0+eps] under x is an interval [0, m] so it contains the two
    reciprocals for all large n. The values y = +1 and -1 along sequences tending to t_0 contradict
    continuity at t_0, where y(t_0) = 0 because x(t_0) = 0 forces the point (0,0). Statement
    unchanged; the card says the argument is its own.
---

::: {.problem}
Optional: Explain why the “topologist’s sine wave” $$X=\{(0,0)\}\cup\{(x,\sin(1/x)):x>0\}$$ is an example of a space which is connected but not path connected.
:::

::: {.solution}
The graph $G=\{(x,\sin(1/x)):x>0\}$ is homeomorphic to $(0,\infty)$, so connected, and adding the limit point $(0,0)$ keeps it connected; but no path can start at $(0,0)$ and reach $G$, since along such a path the first coordinate would have to pass through the zeros of $\sin(1/x)$ with alternating values $\pm1$ accumulating at the start. The argument is this card's own: no retained solution set covers this worksheet.

::: pf

::: {.pf-step #graph}
$G=\{(x,\sin(1/x)):x>0\}$ is homeomorphic to $(0,\infty)$, hence path connected and connected.

::: pf-proof
The map $\varphi\colon(0,\infty)\to G$, $\varphi(x)=(x,\sin(1/x))$, is a bijection with inverse the restriction of the first-coordinate projection $(x,y)\mapsto x$ to $G$, which is continuous as a restriction of a continuous map, and $\varphi$ is continuous because both coordinates are. So $\varphi$ is a homeomorphism, and $(0,\infty)$ is path connected (it is convex), so $G$ is path connected; a path-connected space is connected.
:::

:::


::: {.pf-step #closure}
$(0,0)\in\overline G$ and $X=G\cup\{(0,0)\}$ is connected.

::: pf-proof
With $x_n=1/(n\pi)\to0$ one has $(x_n,\sin(1/x_n))=(x_n,0)\to(0,0)$, so $(0,0)$ is a limit point of $G$. If $A$ is connected and $A\subseteq X\subseteq\overline A$ then $X$ is connected, since $\overline A$ is connected and $X$ lies between a connected set and its closure; applying this with $A=G$ gives that $X$ is connected.
:::

:::


::: {.pf-step #nopath}
There is no path in $X$ from $(0,0)$ to a point of $G$.

::: pf-proof
Suppose $\gamma(t)=(x(t),y(t))$ is a continuous path with $\gamma(0)=(0,0)$ and $\gamma(1)\in G$. The set $Z=\{t\in[0,1]:x(t)=0\}$ is closed in $[0,1]$ and nonempty, since it contains $0$; let $t_0=\sup Z$. Then $t_0\in Z$ by closedness. Since $\gamma(1)\in G$ has positive first coordinate, $t_0<1$. For $t\in(t_0,1]$, $x(t)\ne0$, and $x$ is continuous with $x(t_0)=0$, so by the intermediate value theorem $x(t)>0$ on $(t_0,1]$: indeed $x$ cannot be negative there, since a point with $x<0$ is not in $X$ at all, and it cannot be $0$ by the definition of $t_0$. Hence $y(t)=\sin(1/x(t))$ for $t\in(t_0,1]$.
:::

:::


::: {.pf-step #oscillation}
For $t\to t_0^+$ the values $y(t)$ have both $+1$ and $-1$ as limits along sequences, so $y$ is not continuous at $t_0$; this contradicts the continuity of $\gamma$.

::: pf-proof
Since $x(t)\to0^+$ as $t\to t_0^+$, the image of $[t_0,t_0+\varepsilon]$ under $x$ is, by the intermediate value theorem, an interval $[0,m_\varepsilon]$ with $m_\varepsilon>0$ (it is connected and contains $0$ and a positive value). For every large $n$ the numbers $1/(\pi/2+2\pi n)$ and $1/(3\pi/2+2\pi n)$ lie in $(0,m_\varepsilon)$, so there are $t_n,s_n\in[t_0,t_0+\varepsilon]$ with $x(t_n)=1/(\pi/2+2\pi n)$ and $x(s_n)=1/(3\pi/2+2\pi n)$; then $y(t_n)=\sin(\pi/2+2\pi n)=1$ and $y(s_n)=\sin(3\pi/2+2\pi n)=-1$. Taking $\varepsilon\to0$ gives sequences $t_n,s_n\to t_0$ with $y(t_n)=1$ and $y(s_n)=-1$, while $y(t_0)=0$, since $x(t_0)=0$ forces $\gamma(t_0)=(0,0)$. A function continuous at $t_0$ cannot take both $1$ and $-1$ arbitrarily close to $t_0$, so $y$ is discontinuous at $t_0$, contradicting the continuity of $\gamma$. So no such path exists.
:::

:::


::: {.pf-step #conclusion}
$X$ is connected but not path connected.

::: pf-proof
Connected by step [](#closure){.pf-ref}; not path connected because any two points in a path-connected space are joined by a path, and step [](#nopath){.pf-ref} shows no path joins $(0,0)$ to a point of $G$. Note $X$ is connected but its two "pieces" cannot be separated, which is exactly the phenomenon the example illustrates.
:::

:::

:::
:::
