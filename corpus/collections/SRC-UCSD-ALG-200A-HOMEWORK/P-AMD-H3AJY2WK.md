---
schema: qual/card@1
id: P-AMD-H3AJY2WK
kind: problem
title: Orbits of a normal subgroup in a transitive $G$-set
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 1. Restored
    the source's orbit set Y of H-orbits and the two parts concerning the
    induced G-action, equal orbit cardinalities, and the two index formulas.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used normality to identify g(Hx)=H(gx), then identified the stabilizers
    H_x=H\cap G_x and Stab_G(Hx)=HG_x. Orbit-stabilizer for the restricted
    H-action and the induced transitive G-action gives the two formulas.
---

::: {.problem}
Assume that $G$ acts transitively on a set $X$, and let $H\normal G$.
Restrict the action to $H$, and let
\[
Y=\{\mathcal O_\alpha\}_{\alpha\in I}
\]
be the set of $H$-orbits in $X$.

1. For $g\in G$ and an $H$-orbit $\mathcal O_\alpha$, define
   \[
   g\mathcal O_\alpha=\{gx:x\in\mathcal O_\alpha\}.
   \]
   Show that $g\mathcal O_\alpha$ is again an $H$-orbit, that this rule defines an action of $G$ on $Y$, and that this action is transitive.
   Conclude that all $H$-orbits in $X$ have the same cardinality.

2. If $x\in\mathcal O_\alpha$, prove
   \[
   |\mathcal O_\alpha|=|H:H\cap G_x|
   \qquad\text{and}\qquad
   |Y|=|G:HG_x|,
   \]
   where
   \[
   G_x=\{g\in G:gx=x\}.
   \]
:::

::: {.solution}
For $x\in X$, write
\[
\mathcal O_x=Hx=\{hx:h\in H\}
\]
for its $H$-orbit.

<1>1. For every $g\in G$ and $x\in X$,
\[
g\mathcal O_x=\mathcal O_{gx}.
\]
::: {.proof}
Since $H\normal G$,
\[
gHg^{-1}=H.
\]
Therefore
\[
\begin{aligned}
g\mathcal O_x
&=g(Hx)\\
&=\{ghx:h\in H\}\\
&=\{(ghg^{-1})(gx):h\in H\}\\
&=H(gx)\\
&=\mathcal O_{gx}.
\end{aligned}
\]
Thus $g$ sends every $H$-orbit onto another $H$-orbit.
:::

<1>2. The rule
\[
g\cdot\mathcal O_x:=g\mathcal O_x
\]
defines an action of $G$ on $Y$.
::: {.proof}
By <1>1, the rule takes $Y$ to itself.
For the identity element,
\[
e\cdot\mathcal O_x=\mathcal O_x.
\]
For $g_1,g_2\in G$,
\[
g_1\cdot(g_2\cdot\mathcal O_x)
=g_1(g_2\mathcal O_x)
=(g_1g_2)\mathcal O_x
=(g_1g_2)\cdot\mathcal O_x.
\]
Hence the action axioms hold.
:::

<1>3. The induced action of $G$ on $Y$ is transitive.
::: {.proof}
Let $\mathcal O_x,\mathcal O_y\in Y$.
Because the original $G$-action on $X$ is transitive, there exists $g\in G$ with
\[
gx=y.
\]
Then <1>1 gives
\[
g\mathcal O_x=\mathcal O_{gx}=\mathcal O_y.
\]
Thus every $H$-orbit can be carried to every other one.
:::

<1>4. All $H$-orbits in $X$ have the same cardinality.
::: {.proof}
Let $\mathcal O_x,\mathcal O_y\in Y$.
By <1>3, choose $g\in G$ such that
\[
g\mathcal O_x=\mathcal O_y.
\]
The map
\[
\mathcal O_x\longrightarrow\mathcal O_y,
\qquad
z\longmapsto gz
\]
is bijective, with inverse $z\mapsto g^{-1}z$.
Hence
\[
|\mathcal O_x|=|\mathcal O_y|.
\]
:::

<1>5. If $x\in\mathcal O_\alpha$, then
\[
|\mathcal O_\alpha|=|H:H\cap G_x|.
\]
::: {.proof}
Since $x\in\mathcal O_\alpha$, we have
\[
\mathcal O_\alpha=Hx.
\]
The stabilizer of $x$ for the restricted $H$-action is
\[
H_x=\{h\in H:hx=x\}=H\cap G_x.
\]
The orbit-stabilizer bijection therefore gives
\[
Hx\cong H/(H\cap G_x)
\]
as sets, and hence
\[
|\mathcal O_\alpha|=|H:H\cap G_x|.
\]
:::

<1>6. The subgroup $HG_x$ is the stabilizer in $G$ of the orbit $\mathcal O_x$.
::: {.proof}
Because $H\normal G$, the product $HG_x$ is a subgroup of $G$.

Now let $g\in G$.
By <1>1,
\[
g\mathcal O_x=\mathcal O_{gx}.
\]
Therefore
\[
\begin{aligned}
g\mathcal O_x=\mathcal O_x
&\iff gx\in Hx\\
&\iff gx=hx\text{ for some }h\in H\\
&\iff h^{-1}g\in G_x\text{ for some }h\in H\\
&\iff g\in HG_x.
\end{aligned}
\]
Thus
\[
\operatorname{Stab}_G(\mathcal O_x)=HG_x.
\]
:::

<1>7. We have
\[
|Y|=|G:HG_x|.
\]
::: {.proof}
By <1>3, the $G$-action on $Y$ is transitive.
Hence $Y$ is the orbit of $\mathcal O_x$ under this action.
By <1>6, the stabilizer of $\mathcal O_x$ is $HG_x$.
Orbit-stabilizer therefore gives
\[
|Y|=|G:\operatorname{Stab}_G(\mathcal O_x)|=|G:HG_x|.
\]
:::
:::
