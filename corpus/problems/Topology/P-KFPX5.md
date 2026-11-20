---
schema: qual/card@1
id: P-KFPX5
kind: problem
title: Covering maps inject on $\pi_1$ and are homeomorphisms if they induce $\pi_1$-isomorphisms
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The thirty-three leaf steps of parts (a), (b) and (c) asserted their claim with no proof body;
    each now carries one. No claim is changed: the definition, the statement of the homotopy
    lifting property, the injectivity argument through the lifted homotopy and the two
    bijectivity arguments all stand as they were, and the step numbering is unchanged. Cited by
    number only: Hatcher's Proposition 1.30 for the homotopy lifting property and its path-lifting
    and unique-lifting special cases. Checked: that the even-covering condition makes the fiber
    over an evenly covered set have the cardinality of the index set, that the three edges of the
    lifted square are constant by uniqueness of path lifting, that the fiber is discrete so a
    path in it is constant, and that a locally constant cardinality on the path-connected $X$ is
    constant. Where a step is a definition or the statement of a cited theorem, its proof says
    what the definition or statement carries and why the later steps use it.
---

::: {.problem}
(a) Give the definition of a **covering space** $\widetilde{X}$ (and **covering map** $p: \widetilde{X} \to X$) for a topological space $X$.

(b) State the **homotopy lifting property** of covering spaces. Use it to show that a covering map $p: \widetilde{X} \to X$ induces an injective group homomorphism
$$
p_*: \pi_1(\widetilde{X}, \widetilde{x}_0) \to \pi_1(X, p(\widetilde{x}_0))
$$
on fundamental groups.

(c) Let $p: \widetilde{X} \to X$ be a covering map with $\widetilde{X}$ and $X$ path-connected. Suppose that the induced homomorphism $p_*$ on fundamental groups is an isomorphism. Prove that $p$ is a homeomorphism.
:::

::: {.solution}

Throughout, a loop is a continuous map $[0,1]\to$ the space carrying its endpoints to the basepoint, and $[\,\cdot\,]$ denotes its path-homotopy class.

::: pf

::: pf-step

(a) The definition of a covering space and a covering map is as follows.

::: pf-proof

::: pf-step

Let $X$ be a topological space. A covering space of $X$ consists of a topological space $\widetilde{X}$ and a continuous surjective map $p: \widetilde{X} \to X$ such that every point $x \in X$ has an open neighborhood $U \subseteq X$ that is evenly covered by $p$.

::: pf-proof
This is the definition, so there is nothing to deduce; what it says is that the local structure of $p$ is that of a projection $U\times A\to U$ with $A$ discrete, and that is the property every later step uses. The clause that $p$ be surjective is in fact a consequence of the even-covering clause when $X\ne\varnothing$: if $U$ is evenly covered and $x\in U$, the sheet over $U$ meeting $p^{-1}(x)$ supplies a preimage of $x$. Keeping surjectivity among the hypotheses costs nothing and covers the empty case.
:::

:::

::: pf-step

An open set $U \subseteq X$ is evenly covered if the preimage $p^{-1}(U)$ can be expressed as a disjoint union of open subsets in $\widetilde{X}$:
$$p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha,$$
such that for each index $\alpha \in A$, the restriction $p\restrict_{V_\alpha}: V_\alpha \to U$ is a homeomorphism.

::: pf-proof
Again a definition, and the content that later steps read off it is this. Each $V_\alpha$ is open and the union is disjoint and equals $p^{-1}(U)$; so for $x\in U$ the fiber $p^{-1}(x)$ meets each $V_\alpha$ in exactly one point, namely the image of $x$ under the inverse homeomorphism $(p\restrict_{V_\alpha})^{-1}$, and meets no point outside the union. Hence the cardinality of $p^{-1}(x)$ is that of the index set $A$, the same for every $x\in U$.
:::

:::

::: pf-step

The map $p$ is called a covering map, $X$ is the base space, and the sets $V_\alpha$ are called the sheets of the covering over $U$.

::: pf-proof
This fixes terminology for the rest of the card. The mathematical point carried by the naming is that each sheet is open in $\widetilde{X}$ and, being the complement in $p^{-1}(U)$ of the union of the other sheets, is also closed in $p^{-1}(U)$; over an evenly covered $U$ the map is the projection of the product $U\times A$ onto its first factor, with $A$ indexing the sheets.
:::

:::

:::

:::

::: pf-step

(b) Covering maps have the following homotopy lifting property.

::: pf-proof

::: pf-step

Let $p: \widetilde{X} \to X$ be a covering map, let $Y$ be a topological space, let $f: Y \to \widetilde{X}$ be a continuous map, and let $H: Y \times [0, 1] \to X$ be a continuous homotopy such that $H(y, 0) = p(f(y))$ for all $y \in Y$.

::: pf-proof
These are the data of the property: a map into the base of the covering and a homotopy into the base whose initial slice is the projection of a map $f$ into the total space. The condition $H(y,0)=p(f(y))$ says exactly that $f$ is a lift of the initial map $H(\,\cdot\,,0)$, so the statement below asserts that a lift of the initial slice extends to a lift of the whole homotopy.
:::

:::

::: pf-step

Then there exists a unique continuous homotopy $\widetilde{H}: Y \times [0, 1] \to \widetilde{X}$ such that $\widetilde{H}(y, 0) = f(y)$ for all $y \in Y$ and $p \circ \widetilde{H} = H$.

::: pf-proof
This is the homotopy lifting property of a covering map, stated and cited here rather than proved: it is Hatcher's Proposition 1.30, and the path-lifting and unique-lifting statements used below are its special cases $Y$ a point and $Y=[0,1]$. The two clauses are what the property delivers: existence of a lift agreeing with $f$ on the initial slice, and uniqueness of such a lift.
:::

:::

:::

:::

::: pf-step

(b) The homomorphism $p_*: \pi_1(\widetilde{X}, \widetilde{x}_0) \to \pi_1(X, x_0)$ is injective.

::: pf-proof

::: pf-step

Let $x_0 = p(\widetilde{x}_0)$. Let $[\gamma] \in \pi_1(\widetilde{X}, \widetilde{x}_0)$ be represented by a continuous loop $\gamma: [0, 1] \to \widetilde{X}$ with $\gamma(0) = \gamma(1) = \widetilde{x}_0$.

::: pf-proof
By definition $\pi_1(\widetilde{X},\widetilde{x}_0)$ is the set of path-homotopy classes of loops at $\widetilde{x}_0$, so a class has a representative $\gamma$, and $\gamma$ is continuous with both endpoints at $\widetilde{x}_0$. The map $p_*$ sends $[\gamma]$ to $[p\circ\gamma]$, a class of loops at $p(\gamma(0))=x_0$.
:::

:::

::: pf-step

Suppose $[\gamma] \in \ker p_*$, which means $p_*([\gamma]) = [p \circ \gamma] = [c_{x_0}] \in \pi_1(X, x_0)$, where $c_{x_0}$ is the constant loop at $x_0$.

::: pf-proof
The kernel of a group homomorphism is the preimage of the identity element, and the identity of $\pi_1(X,x_0)$ is the class of the constant loop at $x_0$. So the supposition is the displayed equation, and the rest of the argument derives $[\gamma]=0$ from it.
:::

:::

::: pf-step

This means there is a basepoint-preserving homotopy of paths $H: [0, 1] \times [0, 1] \to X$ such that:
$$H(s, 0) = (p \circ \gamma)(s), \quad H(s, 1) = x_0, \quad H(0, t) = x_0, \quad H(1, t) = x_0 \quad \text{for all } s, t \in [0, 1].$$

::: pf-proof
Two loops at $x_0$ are path-homotopic exactly when there is a homotopy between them through loops at $x_0$: the first two displayed conditions say the homotopy runs from $p\circ\gamma$ to the constant loop, and the last two say the basepoint is fixed throughout, which is what "path-homotopy relative to the endpoints" adds to a free homotopy.
:::

:::

::: pf-step

Applying the homotopy lifting property with $Y = [0, 1]$ and initial map $\gamma: [0, 1] \to \widetilde{X}$, there exists a unique continuous lift $\widetilde{H}: [0, 1] \times [0, 1] \to \widetilde{X}$ with $\widetilde{H}(s, 0) = \gamma(s)$ and $p \circ \widetilde{H} = H$.

::: pf-proof
The homotopy lifting property of the step above requires a homotopy into $X$ whose initial slice is the projection of a map into $\widetilde{X}$; here the homotopy is $H$ and the map is $\gamma$, and $H(s,0)=p(\gamma(s))$ is the first condition of step 2.3. So the property applies verbatim and yields $\widetilde H$ with the two displayed properties.
:::

:::

::: pf-step

Consider the path $t \mapsto \widetilde{H}(0, t)$. It is a lift of the constant path $t \mapsto H(0, t) = x_0$ starting at $\widetilde{H}(0, 0) = \gamma(0) = \widetilde{x}_0$. By uniqueness of path lifting, $\widetilde{H}(0, t) = \widetilde{x}_0$ for all $t \in [0, 1]$.

::: pf-proof
The composite $t\mapsto\widetilde H(0,t)$ is continuous, its projection is $t\mapsto H(0,t)=x_0$, and it starts at $\gamma(0)=\widetilde x_0$ because $\widetilde H(s,0)=\gamma(s)$. The constant path at $\widetilde x_0$ is another lift of the same path with the same initial point, and two lifts of a path from the same point agree by the uniqueness clause of the path-lifting statement, which is the case $Y$ a point of the property.
:::

:::

::: pf-step

Similarly, the path $t \mapsto \widetilde{H}(1, t)$ is a lift of the constant path $t \mapsto H(1, t) = x_0$ starting at $\widetilde{H}(1, 0) = \gamma(1) = \widetilde{x}_0$, so $\widetilde{H}(1, t) = \widetilde{x}_0$ for all $t \in [0, 1]$.

::: pf-proof
Same argument as the preceding step with $s=1$: the projection is the constant path at $x_0$ by step 2.3, and the initial point is $\widetilde H(1,0)=\gamma(1)=\widetilde x_0$ because $\gamma$ is a loop at $\widetilde x_0$.
:::

:::

::: pf-step

At $t = 1$, $s \mapsto \widetilde{H}(s, 1)$ is a lift of the constant path $s \mapsto H(s, 1) = x_0$ starting at $\widetilde{H}(0, 1) = \widetilde{x}_0$, so $\widetilde{H}(s, 1) = \widetilde{x}_0$ for all $s \in [0, 1]$.

::: pf-proof
The projection is $s\mapsto H(s,1)=x_0$ by step 2.3, and the initial point is $\widetilde H(0,1)=\widetilde x_0$ by step 2.5. The constant path at $\widetilde x_0$ is again a lift with the same initial point, so uniqueness of path lifting gives the conclusion.
:::

:::

::: pf-step

Thus $\widetilde{H}$ is a basepoint-preserving homotopy of loops in $\widetilde{X}$ between $\gamma$ and the constant loop $c_{\widetilde{x}_0}$, proving $[\gamma] = 0 \in \pi_1(\widetilde{X}, \widetilde{x}_0)$.

::: pf-proof
$\widetilde H$ is continuous and satisfies $p\circ\widetilde H=H$; by steps 2.5, 2.6 and 2.7 its restrictions to the three edges $s=0$, $s=1$ and $t=1$ are constant at $\widetilde x_0$, and by construction the edge $t=0$ is $\gamma$. So $\widetilde H$ is a homotopy of loops at $\widetilde x_0$ from $\gamma$ to the constant loop, which is precisely the relation $[\gamma]=[c_{\widetilde x_0}]$, the identity of the group.
:::

:::

::: pf-step

Therefore $\ker p_* = \{0\}$, so $p_*$ is injective.

::: pf-proof
Step 2.1 began with an arbitrary class $[\gamma]$ and step 2.8 showed that membership in the kernel forces it to be the identity; so the kernel contains only the identity. A group homomorphism with trivial kernel is injective, since $p_*(a)=p_*(b)$ gives $p_*(ab^{-1})=0$, hence $ab^{-1}=0$, hence $a=b$.
:::

:::

:::

:::

::: {.pf-step #s4}

(c) The covering map $p$ is a bijection.

::: pf-proof

::: pf-step

Fix a basepoint $\widetilde{x}_0 \in \widetilde{X}$ and let $x_0 = p(\widetilde{x}_0)$. We show that the fiber $p^{-1}(x_0)$ consists only of the single point $\widetilde{x}_0$.

::: pf-proof
It is enough to prove this for one point $x_0$ because $X$ is path-connected and the cardinality of the fiber is locally constant, which step 4.11 then uses to propagate the conclusion to every point of $X$. Nothing is assumed about $\widetilde x_0$ beyond its lying over $x_0$.
:::

:::

::: pf-step

Let $\widetilde{x}_1 \in p^{-1}(x_0)$ be any point in the fiber.

::: pf-proof
The fiber is nonempty — it contains $\widetilde x_0$ — and $\widetilde x_1$ denotes an arbitrary element of it, so an argument that forces $\widetilde x_1=\widetilde x_0$ forces the fiber to be a singleton.
:::

:::

::: pf-step

Since $\widetilde{X}$ is path-connected, there exists a continuous path $\widetilde{\alpha}: [0, 1] \to \widetilde{X}$ from $\widetilde{x}_0$ to $\widetilde{x}_1$ (so $\widetilde{\alpha}(0) = \widetilde{x}_0$ and $\widetilde{\alpha}(1) = \widetilde{x}_1$).

::: pf-proof
Path-connectedness of $\widetilde X$ says exactly that any two of its points are joined by a continuous path; apply it to the two points $\widetilde x_0$ and $\widetilde x_1$, both of which lie in $\widetilde X$ because the second was taken in the fiber over $x_0$.
:::

:::

::: pf-step

The projected path $\alpha = p \circ \widetilde{\alpha}: [0, 1] \to X$ satisfies $\alpha(0) = p(\widetilde{x}_0) = x_0$ and $\alpha(1) = p(\widetilde{x}_1) = x_0$, so $\alpha$ is a loop based at $x_0$, representing $[\alpha] \in \pi_1(X, x_0)$.

::: pf-proof
$p\circ\widetilde\alpha$ is continuous as a composite of continuous maps, and its endpoints are $p(\widetilde\alpha(0))=p(\widetilde x_0)=x_0$ and $p(\widetilde\alpha(1))=p(\widetilde x_1)=x_0$, the second because $\widetilde x_1$ was chosen in $p^{-1}(x_0)$. A path whose two endpoints coincide with $x_0$ is a loop at $x_0$, hence represents a class in $\pi_1(X,x_0)$.
:::

:::

::: pf-step

By hypothesis, $p_*: \pi_1(\widetilde{X}, \widetilde{x}_0) \to \pi_1(X, x_0)$ is an isomorphism, so it is surjective. Thus there exists a loop class $[\beta] \in \pi_1(\widetilde{X}, \widetilde{x}_0)$ such that $p_*([\beta]) = [\alpha]$.

::: pf-proof
An isomorphism is in particular surjective, and $[\alpha]$ lies in the target by step 4.4, so it has a preimage $[\beta]$ under $p_*$; that is the displayed equation, and $\beta$ is a loop at $\widetilde x_0$ representing its class.
:::

:::

::: pf-step

This means the loop $p \circ \beta$ is path-homotopic to $\alpha$ in $X$ via a path-homotopy $H: [0, 1] \times [0, 1] \to X$ with $H(s, 0) = \alpha(s)$ and $H(s, 1) = (p \circ \beta)(s)$, keeping endpoints fixed at $x_0$.

::: pf-proof
$p_*([\beta])=[p\circ\beta]$ by definition, so the equation of step 4.5 reads $[p\circ\beta]=[\alpha]$, which by the definition of path-homotopy of loops means there is a homotopy $H$ between the two loops with $H(s,0)=\alpha(s)$, $H(s,1)=(p\circ\beta)(s)$ and $H(0,t)=H(1,t)=x_0$ throughout.
:::

:::

::: pf-step

By the homotopy lifting property, $H$ lifts to a homotopy $\widetilde{H}: [0, 1] \times [0, 1] \to \widetilde{X}$ with $\widetilde{H}(s, 0) = \widetilde{\alpha}(s)$.

::: pf-proof
The property is applied with $Y=[0,1]$, with $f=\widetilde\alpha$ and with the homotopy $H$ of step 4.6; its hypothesis holds because $H(s,0)=\alpha(s)=p(\widetilde\alpha(s))$ by step 4.4. The lift satisfies $p\circ\widetilde H=H$ and agrees with $\widetilde\alpha$ on the initial slice, which is the displayed condition.
:::

:::

::: pf-step

The path $t \mapsto \widetilde{H}(0, t)$ lifts the constant path at $x_0$ from $\widetilde{x}_0$, so it is constant at $\widetilde{x}_0$. Hence $s \mapsto \widetilde{H}(s, 1)$ is the lift of $p \circ \beta$ starting at $\widetilde{x}_0$, which is the loop $\beta$ by uniqueness of path lifting, so $\widetilde{H}(1, 1) = \beta(1) = \widetilde{x}_0$.

::: pf-proof
The basepoint edge $H(0,t)=x_0$ is constant by step 4.6, and $\widetilde H(0,0)=\widetilde\alpha(0)=\widetilde x_0$, so uniqueness of path lifting gives $\widetilde H(0,t)=\widetilde x_0$. Hence the path $s\mapsto\widetilde H(s,1)$ starts at $\widetilde H(0,1)=\widetilde x_0$ and projects to $s\mapsto H(s,1)=(p\circ\beta)(s)$; the loop $\beta$ itself is a lift of $p\circ\beta$ with the same initial point $\beta(0)=\widetilde x_0$, so the two agree. Evaluating at $s=1$ gives $\widetilde H(1,1)=\beta(1)=\widetilde x_0$.
:::

:::

::: pf-step

Since $\widetilde{H}(1, t)$ must be constant in the discrete fiber $p^{-1}(x_0)$, $\widetilde{x}_1 = \widetilde{\alpha}(1) = \widetilde{H}(1, 0) = \widetilde{H}(1, 1) = \widetilde{x}_0$.

::: pf-proof
The path $t\mapsto\widetilde H(1,t)$ lies in $p^{-1}(x_0)$ because its projection is $t\mapsto H(1,t)=x_0$; the fiber is discrete, since an evenly covered neighbourhood $U$ of $x_0$ has $p^{-1}(U)$ a disjoint union of sheets each meeting the fiber in one point, so each point of the fiber has a neighbourhood meeting it in that point alone. A continuous map from the connected interval into a discrete space is constant, so $\widetilde H(1,0)=\widetilde H(1,1)$; and $\widetilde H(1,0)=\widetilde\alpha(1)=\widetilde x_1$ by step 4.7, while $\widetilde H(1,1)=\widetilde x_0$ by step 4.8.
:::

:::

::: pf-step

Thus $p^{-1}(x_0) = \{\widetilde{x}_0\}$ is a singleton.

::: pf-proof
Step 4.2 took an arbitrary $\widetilde x_1\in p^{-1}(x_0)$ and step 4.9 showed $\widetilde x_1=\widetilde x_0$; so every element of the fiber is $\widetilde x_0$, and the fiber is nonempty.
:::

:::

::: pf-step

Since $X$ is path-connected and the cardinality of the fiber $p^{-1}(x)$ is locally constant, $\cardinality{p^{-1}(x)} = 1$ for all $x \in X$. Thus $p$ is a bijection.

::: pf-proof
Local constancy: for an evenly covered open $U$ and any $y\in U$, step 1.2 shows that $\cardinality{p^{-1}(y)}$ equals the number of sheets over $U$, the same number for every $y\in U$. A locally constant function on the path-connected space $X$ is constant, so its value at $x_0$, which is $1$ by step 4.10, is its value everywhere. A map all of whose fibers are singletons is injective (two points in one fiber would force them equal) and surjective (the fiber over any point is nonempty, containing its single element).
:::

:::

:::

:::

::: pf-step

(c) The bijective covering map $p$ is a homeomorphism.

::: pf-proof

::: pf-step

The map $p: \widetilde{X} \to X$ is continuous and bijective by step [](#s4){.pf-ref}.

::: pf-proof
Continuity is part of the definition of a covering map, recorded in step 1.1; bijectivity is the conclusion of step [](#s4){.pf-ref}, which showed every fiber to be a singleton.
:::

:::

::: pf-step

To show that $p$ is a homeomorphism, it suffices to prove that $p$ is an open map.

::: pf-proof
A continuous bijection whose inverse is continuous is a homeomorphism, and the inverse is continuous exactly when $p$ carries open sets to open sets: for open $W\subseteq\widetilde X$, the preimage of $W$ under $p^{-1}$ is $p(W)$, so continuity of $p^{-1}$ is openness of $p$.
:::

:::

::: pf-step

Let $W \subseteq \widetilde{X}$ be an open set, and let $x \in p(W)$. Choose $\widetilde{w} \in W$ such that $p(\widetilde{w}) = x$.

::: pf-proof
$x\in p(W)$ means by definition that $x=p(\widetilde w)$ for some $\widetilde w\in W$, so such a point exists; the rest of the argument shows that a whole neighbourhood of $x$ lies in $p(W)$, which is what makes $p(W)$ open at each of its points.
:::

:::

::: pf-step

Let $U$ be an evenly covered open neighborhood of $x$ in $X$. Since $\cardinality{p^{-1}(x)} = 1$, $p^{-1}(U) = V$ consists of a single open sheet $V \subseteq \widetilde{X}$, and $p\restrict_V: V \to U$ is a homeomorphism.

::: pf-proof
An evenly covered neighbourhood exists at every point of $X$ by step 1.1. Write $p^{-1}(U)=\bigsqcup_\alpha V_\alpha$ as in step 1.2; each $V_\alpha$ meets $p^{-1}(x)$ in exactly one point, and $p^{-1}(x)$ has exactly one point by step 4.11, so there is exactly one index $\alpha$ with $V_\alpha\ne\varnothing$. Hence $p^{-1}(U)=V$ for that single sheet, and $p\restrict_V:V\to U$ is a homeomorphism by the definition of a sheet.
:::

:::

::: pf-step

The set $W \cap V$ is an open neighborhood of $\widetilde{w}$ in $V$.

::: pf-proof
$W$ is open in $\widetilde X$ and $V$ is open in $\widetilde X$, so $W\cap V$ is open in $\widetilde X$ and therefore open in the subspace $V$. It contains $\widetilde w$ because $\widetilde w\in W$ by step 5.3 and $\widetilde w\in p^{-1}(x)\subseteq p^{-1}(U)=V$ because $p(\widetilde w)=x$.
:::

:::

::: pf-step

Since $p\restrict_V$ is a homeomorphism, $p(W \cap V)$ is open in $U$, and hence open in $X$.

::: pf-proof
A homeomorphism carries open sets to open sets, so the image of the set of step 5.5, open in $V$, is open in $U$. Since $U$ is open in $X$, an open subset of $U$ is open in $X$: it is $U\cap O$ for an open $O\subseteq X$.
:::

:::

::: pf-step

Since $x = p(\widetilde{w}) \in p(W \cap V) \subseteq p(W)$, $p(W)$ is a neighborhood of each of its points, so $p(W)$ is open in $X$.

::: pf-proof
$\widetilde w\in W\cap V$ by step 5.5, so $x=p(\widetilde w)\in p(W\cap V)$, and $p(W\cap V)\subseteq p(W)$ because $W\cap V\subseteq W$. Step 5.6 gives an open set $p(W\cap V)$ containing $x$ and contained in $p(W)$; since $x$ was an arbitrary point of $p(W)$, every point of $p(W)$ is interior to it.
:::

:::

::: pf-step

Therefore $p$ is an open continuous bijection, so $p$ is a homeomorphism.

::: pf-proof
Openness is step 5.7, continuity and bijectivity are step 5.1, and step 5.2 turns the three into the statement that $p$ has a continuous inverse, which is what it means for $p$ to be a homeomorphism.
:::

:::

:::

:::

:::

:::
