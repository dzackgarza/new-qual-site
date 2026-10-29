---
schema: qual/card@1
id: P-WESTOP13-I3
kind: problem
title: Connected, path-connected, and quasi-components of unions of concentric circles
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $C_r$ denote the circle of radius $r$ centered at the origin in $\RR^2$. Determine the connected components, path-connected components, and quasi-components of each of the following subspaces:

1. \[
   S=\bigcup_{n\ge1}C_{1/n}\cup\{(0,0),(1,1)\};
   \]
2. \[
   T=\bigcup_{\substack{r\in\QQ\\0<r<1}}C_r\cup\{(-1,0),(0,0),(1,0)\}.
   \]
:::

::: {.solution}

Let
$$
\rho:\RR^2\to[0,\infty),
\qquad
\rho(x)=\|x\|.
$$

::: pf

::: {.pf-step #s1-1}

The connected components and path-connected components of $S$ are
$$
\boxed{
C_{1/n}\ (n\ge1),
\qquad
\{(0,0)\},
\qquad
\{(1,1)\}.}
$$


::: pf-proof

The radial image of $S$ is
$$
\rho(S)=\{0\}\cup\{1/n:n\ge1\}\cup\{\sqrt2\}.
$$
This subspace of $\RR$ is totally disconnected. If $A\subseteq S$ is connected, then the continuous image $\rho(A)$ is connected, hence is a singleton. Therefore every connected subset of $S$ lies in one radial fiber.

For radius $1/n$, the fiber is the whole circle $C_{1/n}$, which is path-connected. The fibers at radii $0$ and $\sqrt2$ are respectively the singletons $\{(0,0)\}$ and $\{(1,1)\}$. Thus these fibers are exactly the connected components. Since each is path-connected, they are also exactly the path-connected components.

:::

:::

::: {.pf-step #s1-2}

The quasi-components of $S$ are the same sets as in step [](#s1-1){.pf-ref}.


::: pf-proof

The space
$$
\bigcup_{n\ge1}C_{1/n}\cup\{(0,0)\}
$$
is closed and bounded in $\RR^2$, hence compact, and adjoining the isolated point $(1,1)$ preserves compactness. Thus $S$ is compact Hausdorff. In every compact Hausdorff space, quasi-components coincide with connected components. Step [](#s1-1){.pf-ref} therefore gives the quasi-components.

Equivalently, one can see this directly: each circle $C_{1/n}$ and the point $(1,1)$ can be isolated by clopen radial neighborhoods, while clopen sets
$$
S\cap\rho^{-1}([0,a))
$$
with $a>0$ chosen between successive radii shrink to $(0,0)$.

:::

:::

::: {.pf-step #s1-3}

The connected components and path-connected components of $T$ are
$$
\boxed{
C_r\quad(r\in\QQ,\ 0<r<1),
\qquad
\{(0,0)\},
\qquad
\{(1,0)\},
\qquad
\{(-1,0)\}.}
$$


::: pf-proof

The radial image is
$$
\rho(T)=\bigl(\QQ\cap(0,1)\bigr)\cup\{0,1\},
$$
which is totally disconnected. Hence every connected subset of $T$ lies in one radial fiber.

For rational $0<r<1$, the fiber is $C_r$, which is path-connected. The fiber at radius $0$ is the singleton $\{(0,0)\}$. The radius-$1$ fiber is
$$
\{(-1,0),(1,0)\},
$$
whose two points form separate connected components because they have disjoint relative neighborhoods in $T$. Thus the listed sets are the connected components, and each is path-connected, so they are also the path-connected components.

:::

:::

::: {.pf-step #s1-4}

For every rational $r\in(0,1)$, the quasi-component of a point of $C_r$ is exactly $C_r$, and the quasi-component of $(0,0)$ is $\{(0,0)\}$.


::: pf-proof

Each connected component is contained in the corresponding quasi-component, so $C_r$ lies in the quasi-component of each of its points.

If $r\ne s$ are two values in
$$
\bigl(\QQ\cap(0,1)\bigr)\cup\{0,1\},
$$
choose an irrational number $a$ strictly between them. Then
$$
T\cap\rho^{-1}([0,a))
$$
is clopen in $T$: its complement is $T\cap\rho^{-1}((a,\infty))$, and no point of $T$ has radius $a$. Hence points with distinct radii lie in distinct quasi-components. This isolates every $C_r$ from all other radial fibers and, by taking arbitrarily small irrational $a>0$, isolates $(0,0)$ from every other point.

:::

:::

::: {.pf-step #s1-5}

The two points $(1,0)$ and $(-1,0)$ belong to the same quasi-component of $T$.


::: pf-proof

Let $U\subseteq T$ be clopen and suppose $(1,0)\in U$. Since $U$ is open in $T$, there is $\varepsilon>0$ such that
$$
B((1,0),\varepsilon)\cap T\subseteq U.
$$
For every rational $r<1$ sufficiently close to $1$, the circle $C_r$ meets this ball. Since $C_r$ is connected and $U\cap C_r$ is clopen in $C_r$, the nonempty intersection forces
$$
C_r\subseteq U.
$$

Suppose $(-1,0)\notin U$. Because $T\setminus U$ is open, there is $\delta>0$ such that
$$
B((-1,0),\delta)\cap T\subseteq T\setminus U.
$$
For every rational $r<1$ sufficiently close to $1$, the same circle $C_r$ also meets this ball. Choosing $r$ close enough to $1$ to satisfy both requirements gives a circle $C_r$ contained in $U$ but also meeting $T\setminus U$, a contradiction.

Thus every clopen neighborhood of $(1,0)$ contains $(-1,0)$. By symmetry, every clopen neighborhood of $(-1,0)$ contains $(1,0)$. Hence the two points lie in the same quasi-component.

:::

:::

::: {.pf-step #s1-6}

No point of radius less than $1$ lies in the quasi-component from step [](#s1-5){.pf-ref}. Therefore that quasi-component is exactly
$$
\boxed{\{(-1,0),(1,0)\}}.
$$


::: pf-proof

Let $x\in T$ have radius $r<1$. Choose an irrational $a$ with
$$
r<a<1.
$$
Then
$$
T\cap\rho^{-1}((a,\infty))
$$
is a clopen subset of $T$ containing both radius-$1$ points but not $x$. Thus $x$ is not in their quasi-component. Combine this with step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Hence the quasi-components of $T$ are
$$
\boxed{
C_r\quad(r\in\QQ,\ 0<r<1),
\qquad
\{(0,0)\},
\qquad
\{(-1,0),(1,0)\}.}
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give all quasi-components.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} determine all three kinds of components for $S$, and steps [](#s1-3){.pf-ref} through [](#s1-7){.pf-ref} do so for $T$.

:::

:::

:::
