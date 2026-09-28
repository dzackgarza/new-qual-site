---
schema: qual/card@1
id: P-BERK78S-12
kind: problem
title: Real-valued analytic functions are constant, and $\operatorname{Re}g+\operatorname{Im}g$ has open image when $g'\ne0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the open mapping theorem for part 1: a nonconstant analytic image
    would be open in C but is contained in R. For part 2, g' never vanishes,
    so g is nonconstant on every component and g(W) is open. The real
    linear map L(w)=Re(w)+Im(w) sends every open disk to an open interval,
    hence is an open map, so L(g(W)) is open in R.
---

::: {.problem}
1. Suppose $f$ is analytic on a connected open set $U\subset\mathbb C$ and takes only real values. Prove that $f$ is constant.
2. Suppose $W\subset\mathbb C$ is open, $g$ is analytic on $W$, and $g'(z)\ne0$ for every $z\in W$. Show that
   \[
   \{\operatorname{Re}g(z)+\operatorname{Im}g(z):z\in W\}\subset\mathbb R
   \]
   is open in $\mathbb R$.
:::

::: {.solution}
<1>1. If the analytic function $f:U\to\CC$ in part (1) were
nonconstant, then $f(U)$ would be open in $\CC$.

::: {.proof}
The set $U$ is connected and open. By the open mapping theorem, every
nonconstant analytic function on a domain maps open sets to open sets. Thus
a nonconstant $f$ would have open image $f(U)$ in $\CC$.
:::

<1>2. The function $f$ in part (1) is constant.

::: {.proof}
By hypothesis,
$$
f(U)\subseteq\RR.
$$
No nonempty subset of $\RR$ is open in $\CC$: every complex disk around a
real point contains nonreal points. Thus the conclusion of step <1>1 is
impossible unless $f$ is constant. Hence
$$
\boxed{f\text{ is constant}.}
$$
:::

<1>3. For every connected component $C$ of $W$, the restriction
$$
g|_C
$$
is nonconstant.

::: {.proof}
If $g|_C$ were constant, its derivative would vanish everywhere on $C$.
This contradicts the hypothesis
$$
g'(z)\neq0
$$
for every $z\in W$.
:::

<1>4. The set $g(W)$ is open in $\CC$.

::: {.proof}
Every connected component $C$ of the open set $W$ is itself open. By step
<1>3, the restriction $g|_C$ is nonconstant and analytic, so the open
mapping theorem gives that $g(C)$ is open in $\CC$. Since
$$
g(W)
=
\bigcup_C g(C),
$$
the image $g(W)$ is a union of open sets and hence open.
:::

<1>5. Define
$$
L:\CC\longrightarrow\RR,
\qquad
L(w)=\operatorname{Re}w+\operatorname{Im}w.
$$
The map $L$ sends open subsets of $\CC$ to open subsets of $\RR$.

::: {.proof}
Let $O\subseteq\CC$ be open and let
$$
t_0\in L(O).
$$
Choose $w_0\in O$ with $L(w_0)=t_0$. Since $O$ is open, there is
$\varepsilon>0$ such that
$$
B(w_0,\varepsilon)\subseteq O.
$$
For every real $s$ with $\abs{s}<\varepsilon$,
$$
w_0+s\in B(w_0,\varepsilon),
$$
and
$$
L(w_0+s)
=
L(w_0)+s
=
t_0+s.
$$
Therefore
$$
(t_0-\varepsilon,t_0+\varepsilon)
\subseteq
L(O).
$$
Every point of $L(O)$ is thus interior, so $L(O)$ is open in $\RR$.
:::

<1>6. The set
$$
\boxed{
\{
\operatorname{Re}g(z)+\operatorname{Im}g(z):
z\in W
\}
}
$$
is open in $\RR$.

::: {.proof}
The displayed set is exactly
$$
L(g(W)).
$$
Step <1>4 shows that $g(W)$ is open in $\CC$, and step <1>5 shows that
$L$ maps open subsets of $\CC$ to open subsets of $\RR$. Hence
$L(g(W))$ is open.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (1), and step <1>6 proves part (2).
:::
:::
