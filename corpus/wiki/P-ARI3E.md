---
schema: qual/card@1
id: P-ARI3E
kind: problem
title: "Negate $\\forall x\\in \\RR,~\\exists y\\in \\RR \\suchthat \\abs{x-y} \\geq 2017$ $\\exists x\\in \\RR \\suchthat \\forall y\\in \\RR,~ \\abs{x-y} < 2017$ Note that $p\\implies q \\iff q \\vee \\neg p$, so we have\u2026"
classification:
  areas:
  - prelim
  topics:
  - logic-and-quantifiers
relations: []
review: draft
---

::: problem
1. 
   1. Negate $\forall x\in \RR,~\exists y\in \RR \suchthat \abs{x-y} \geq 2017$
   $$\exists x\in \RR \suchthat \forall y\in \RR,~ \abs{x-y} < 2017$$

   1. Note that $p\implies q \iff q \vee \neg p$, so we have $\neg(p \implies q) \iff \neg(q \vee \neg p) \iff p ~\&~ \neg q$.
$$
f: \RR \to \RR \text{ is continuous } \iff \\ 
\forall (x, y) \in \RR^2, ~\forall \varepsilon,~\exists \delta \suchthat \quad d(x,y) < \delta \implies d(f(x), f(y)) < \varepsilon \iff \\ 
\forall (x, y) \in \RR^2, ~\forall \varepsilon,~\exists \delta \suchthat \quad  d(x,y) \geq \delta ~~\vee~~   d(f(x), f(y)) < \varepsilon  ,
$$
so
$$
f: \RR \to \RR \text{ is not continuous } \iff \\ \exists (x,y) \in \RR^2, \exists \varepsilon \suchthat \forall \delta, \quad d(x,y) < \delta ~\&~ d(f(x), f(y)) \geq \varepsilon. \qed
$$

1. $V = \theset{\vector v \in \RR^3 \suchthat \inner{\vector v}{\thevector{3,4,5}} = \vector 0}$
   1. Subspace test: $V \subset X$ is a linear subspace iff $\theset{t\vector v_1 + \vector v_2 \suchthat t\in \RR, \vector v_i \in V} \subseteq V$.
   $$
   \inner{t\vector v_1 + \vector v_2}{\thevector{3,4,5}} = t\inner{\vector v_1}{\thevector{3,4,5}} + \inner{\vector v_2}{\thevector{3,4,5}} = t\vector 0 + \vector 0 = \vector 0.\qed
   $$
      1. Alternatively, just note that it is the kernel of the linear map $\inner{\wait}{\thevector{3,4,5}}: \RR^3 \to \RR^1$, and kernels are always sub-things.
   1. Yes, note $V$ defines a plane $P \cong \RR^2 \subset \RR^3$, so a projection onto $P^\perp = \thevector{3,4,5}$ will work:
   $$
   A = \left[ \begin{array}{ccc} 3 & 4 & 5 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right]
   $$
   Then $A\vector x = \thevector{3x + 4y + 5z, 0, 0}$ and if $\vector x \in V$ then $3x+4y+5z = 0$ by definition and thus $A\vector x = \vector 0$.
   1. Yes, first we look for a matrix that annihilates $\thevector{3,4,5}$ and has rank 2, since its rows will span the 2-dimensional subspace $V$. One that works is
   $$
    A = \left[ \begin{array}{ccc} 2 & 1 & -2 \\ 0 & -5 & 4 \\ 0 & 0 & 0\end{array}\right]
   $$
   So now we know that $\thevector{2,1,-2}, \thevector{0,-5,4} \in V$, and since $A$ is rank 2, they in fact span $V$. Thus we can take $A^T$, whose columns are these vectors. Then the columnspace of $A^T$ is $V$, and thus the linear map corresponding to $A^T$ has image $V$. $\qed$
   1. No, by rank nullity: $\abs{\im A} + \abs{\ker A} = \abs{\mathrm{domain} A}$, but $\abs{V} = 2$, so this would force the contradiction $2+2 = 3$.
   
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. (a) Negate the statement: $\forall x \in \mathbb{R}, \, \exists y \in \mathbb{R} \text{ such that } |x-y| \ge 2017$.
   (b) State and negate the $\varepsilon$-$\delta$ definition of continuity of $f: \mathbb{R} \to \mathbb{R}$.
2. For $V = \{(x,y,z) \in \mathbb{R}^3 \mid 3x+4y+5z=0\}$:
   (a) Show $V$ is a subspace.
   (b) Find a linear map with kernel $V$.
   (c) Find a linear map with image $V$.
   (d) Determine if a linear map exists with both kernel and image equal to $V$.

<1>1. Part 1(a): The negation is $\exists x \in \mathbb{R} \text{ such that } \forall y \in \mathbb{R}, \, |x-y| < 2017$.
    Proof: By De Morgan's laws for quantifiers, $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ and $\neg(\exists y, Q(y)) \iff \forall y, \neg Q(y)$, with $\neg(|x-y| \ge 2017) \iff |x-y| < 2017$.

<1>2. Part 1(b): A function $f: \mathbb{R} \to \mathbb{R}$ is continuous iff $\forall x \in \mathbb{R}, \, \forall \varepsilon > 0, \, \exists \delta > 0, \, \forall y \in \mathbb{R} \, (|x-y|<\delta \implies |f(x)-f(y)|<\varepsilon)$. Its negation is:
    $$\exists x \in \mathbb{R}, \, \exists \varepsilon > 0 \text{ such that } \forall \delta > 0, \, \exists y \in \mathbb{R} \text{ with } |x-y|<\delta \text{ and } |f(x)-f(y)| \ge \varepsilon.$$
    Proof: By quantifier negation and the equivalence $\neg(p \implies q) \iff p \wedge \neg q$.

<1>3. Part 2(a): $V$ is a subspace of $\mathbb{R}^3$.
    Proof: $V = \ker(\phi)$ where $\phi(x,y,z) = 3x+4y+5z$ is a linear functional $\mathbb{R}^3 \to \mathbb{R}$. The kernel of any linear map is a subspace.

<1>4. Part 2(b): $S = \begin{pmatrix} 3 & 4 & 5 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ has $\ker(S) = V$.
    Proof: $S(x,y,z)^T = (3x+4y+5z, 0, 0)^T = \mathbf{0} \iff (x,y,z) \in V$.

<1>5. Part 2(c): $T = \begin{pmatrix} 4 & 5 & 0 \\ -3 & 0 & 0 \\ 0 & -3 & 0 \end{pmatrix}$ has $\operatorname{im}(T) = V$.
    Proof: The columns $v_1 = (4,-3,0)^T$ and $v_2 = (5,0,-3)^T$ are linearly independent vectors in $V$. Since $\dim(V) = 2$, they span $V$.

<1>6. Part 2(d): No linear map $U: \mathbb{R}^3 \to \mathbb{R}^3$ can have $\ker(U) = \operatorname{im}(U) = V$.
    Proof: By Rank-Nullity, $\dim(\ker U) + \dim(\operatorname{im} U) = 3$. But if $\ker(U) = \operatorname{im}(U) = V$, then $\dim(V) + \dim(V) = 2 + 2 = 4 \neq 3$, contradiction. Q.E.D.
:::
