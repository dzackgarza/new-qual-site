---
schema: qual/card@1
id: P-MMAQ-ONJ473ASC7
kind: problem
title: a. Show that $L^2([0, 1]) \subseteq L^1([0, 1])$ and argue that…
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - functional-analysis
  - riesz-representation
relations: []
review: draft
---

::: problem
a.  Show that $L^2([0, 1]) \subseteq L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact
    forms a dense subset of $L^1([0, 1])$.

b.  Let $\Lambda$ be a continuous linear functional on $L^1([0, 1])$.

    Prove the Riesz Representation Theorem for $L^1([0, 1])$ by following the steps below:

    i.  Establish the existence of a function $g \in L^2([0, 1])$ which represents $\Lambda$ in the sense that
        $$
        \Lambda(f ) = f (x)g(x) dx \text{ for all } f \in L^2([0, 1]).
        $$

    > Hint: You may use, without proof, the Riesz Representation Theorem for $L^2([0, 1])$.

    ii. Argue that the $g$ obtained above must in fact belong to $L^\infty([0, 1])$ and represent $\Lambda$ in the sense that
        $$
        \Lambda(f)=\int_{0}^{1} f(x) \overline{g(x)} d x \quad \text { for all } f \in L^{1}([0,1])
        $$
        with
        $$
        \|g\|_{L^{\infty}([0,1])}=\|\Lambda\|_{L^{1}([0,1])\dual}
        $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) Show $L^2([0,1]) \subseteq L^1([0,1])$ and that $L^2$ is dense in $L^1$. (b) For $\Lambda \in (L^1([0,1]))\dual$: (i) find $g \in L^2$ representing $\Lambda$ on $L^2$; (ii) show $g \in L^\infty$, $\Lambda(f) = \int f \overline{g}$ for all $f \in L^1$, and $\norm{g}_\infty = \norm{\Lambda}$.

<1>1. Proof of (a): $L^2([0,1]) \subseteq L^1([0,1])$ and $L^2$ is dense in $L^1$.
    <2>1. For $f \in L^2([0,1])$, $\int_0^1 \abs{f} \leq \left(\int_0^1 \abs{f}^2\right)^{1/2} \left(\int_0^1 1\right)^{1/2} = \norm{f}_2$.
        Proof: Hölder's inequality with $p = q = 2$, and $m([0,1]) = 1$.
    <2>2. Hence $L^2([0,1]) \subseteq L^1([0,1])$ with $\norm{f}_1 \leq \norm{f}_2$.
        Proof: By <2>1, $\norm{f}_1 < \infty$ for $f \in L^2$.
    <2>3. Every $f \in L^1([0,1])$ is approximated in $L^1$ by simple functions, which are bounded, hence in $L^2$.
        Proof: Standard density: simple functions are dense in $L^1$; each simple function $s = \sum c_j \chi_{E_j}$ satisfies $\int \abs{s}^2 = \sum \abs{c_j}^2 m(E_j) < \infty$ since $m(E_j) \leq 1$.
    <2>4. Hence $L^2([0,1])$ is dense in $L^1([0,1])$.
        Proof: For $f \in L^1$ and $\eps > 0$, take a simple $s$ with $\norm{f - s}_1 < \eps$ (<2>3); $s \in L^2$ (<2>3), so the $L^2$-functions approximate $f$.
    <2>5. Q.E.D.
        Proof: This proves (a).

<1>2. Proof of (b)(i): there is $g \in L^2([0,1])$ with $\Lambda(f) = \int_0^1 f \overline{g}$ for all $f \in L^2([0,1])$.
    <2>1. Restrict $\Lambda$ to $L^2([0,1])$; this restriction is a bounded linear functional on $L^2$.
        Proof: For $f \in L^2$, $\abs{\Lambda(f)} \leq \norm{\Lambda} \norm{f}_1 \leq \norm{\Lambda} \norm{f}_2$ by <1>1<2>1, so the restriction is bounded with norm $\leq \norm{\Lambda}$.
    <2>2. By the Riesz Representation Theorem for $L^2$, there is a unique $g \in L^2([0,1])$ with $\Lambda(f) = \int_0^1 f \overline{g}$ for all $f \in L^2([0,1])$, and $\norm{g}_2 = \norm{\Lambda|_{L^2}} \leq \norm{\Lambda}$.
        Proof: The Riesz theorem for Hilbert spaces (given without proof by the problem), plus <2>1 for the norm estimate.
    <2>3. Q.E.D.
        Proof: This proves (b)(i).

<1>3. Proof of (b)(ii), first part: $g \in L^\infty([0,1])$.
    <2>1. Let $M \definedas \norm{\Lambda}$. For $t > M$, define $E_t \definedas \theset{x : \abs{g(x)} > t}$ and $\varphi_t \definedas \chi_{E_t} \overline{g}/\abs{g}$ (the phase of $g$ on $E_t$, zero elsewhere; interpret $0/0 = 0$).
        Proof: Definition. $\varphi_t$ is measurable with $\abs{\varphi_t} = \chi_{E_t}$.
    <2>2. $\varphi_t \in L^2([0,1])$, and $\int_0^1 \varphi_t \overline{g} = \int_{E_t} \abs{g} \geq t \cdot m(E_t)$.
        Proof: $\varphi_t \overline{g} = \chi_{E_t} \abs{g} \geq t \chi_{E_t}$ pointwise; integrability follows from $\abs{\varphi_t \overline{g}} \leq \abs{g} \in L^2 \subseteq L^1$.
    <2>3. $t \cdot m(E_t) \leq \int \varphi_t \overline{g} = \Lambda(\varphi_t) \leq \norm{\Lambda} \norm{\varphi_t}_1 = M \cdot m(E_t)$.
        Proof: The equality is <1>2<2>2 applied to $\varphi_t \in L^2$; the right inequality is boundedness of $\Lambda$ with $\norm{\varphi_t}_1 = m(E_t)$.
    <2>4. If $m(E_t) > 0$, then <2>3 gives $t \leq M$, contradicting $t > M$; hence $m(E_t) = 0$ for all $t > M$.
        Proof: Divide <2>3 by $m(E_t) > 0$.
    <2>5. Hence $\abs{g} \leq M$ almost everywhere, i.e. $g \in L^\infty$ with $\norm{g}_\infty \leq M = \norm{\Lambda}$.
        Proof: $\abs{g} > M$ is the union over $t > M$ (e.g. rational $t$) of the null sets $E_t$, hence null.
    <2>6. Q.E.D.
        Proof: This proves $g \in L^\infty$.

<1>4. Proof of (b)(ii), second part: $\Lambda(f) = \int_0^1 f \overline{g}$ for all $f \in L^1([0,1])$.
    <2>1. The formula holds for $f \in L^2([0,1])$.
        Proof: By <1>2<2>2.
    <2>2. Both sides are continuous linear functionals on $L^1$: $\Lambda$ by hypothesis, and $f \mapsto \int f \overline{g}$ by Hölder, since $g \in L^\infty$ (<1>3).
        Proof: $\abs{\int f \overline{g}} \leq \norm{g}_\infty \norm{f}_1$.
    <2>3. $L^2([0,1])$ is dense in $L^1([0,1])$.
        Proof: By <1>1.
    <2>4. Hence the two functionals agree on all of $L^1$.
        Proof: Two continuous linear functionals agreeing on a dense subspace agree everywhere.
    <2>5. Q.E.D.
        Proof: This proves the representation for all $f \in L^1$.

<1>5. Proof of (b)(ii), third part: $\norm{g}_\infty = \norm{\Lambda}$.
    <2>1. $\norm{\Lambda} \leq \norm{g}_\infty$.
        Proof: For $f \in L^1$, $\abs{\Lambda(f)} = \abs{\int f \overline{g}} \leq \norm{g}_\infty \norm{f}_1$ (<1>4, Hölder); take the sup over $\norm{f}_1 = 1$.
    <2>2. $\norm{g}_\infty \leq \norm{\Lambda}$.
        Proof: By <1>3<2>5.
    <2>3. Q.E.D.
        Proof: Combine <2>1 and <2>2.
:::
