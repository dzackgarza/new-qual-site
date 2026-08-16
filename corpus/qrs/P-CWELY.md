---
schema: qual/card@1
id: P-CWELY
kind: problem
title: "$V = \\theset{\\vector v \\in \\RR^3 \\suchthat \\inner{\\vector v}{\\thevector{3,4,5}} = \\vector 0}$ Subspace test: $V \\subset X$ is a linear subspace iff\u2026"
classification:
  areas:
  - prelim
  topics:
  - vector-spaces
  - linear-algebra
relations: []
review: draft
---

::: problem
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

**Goal:** Let $V = \{(x,y,z) \in \mathbb{R}^3 \mid 3x+4y+5z = 0\}$.
(a) Show that $V$ is a linear subspace of $\mathbb{R}^3$.
(b) Determine whether there exists a linear map $S: \mathbb{R}^3 \to \mathbb{R}^3$ with $\ker(S) = V$.
(c) Determine whether there exists a linear map $T: \mathbb{R}^3 \to \mathbb{R}^3$ with $\operatorname{im}(T) = V$.
(d) Determine whether there exists a linear map $U: \mathbb{R}^3 \to \mathbb{R}^3$ with $\ker(U) = \operatorname{im}(U) = V$.

<1>1. $V$ is a linear subspace of $\mathbb{R}^3$.
    Proof:
    <2>1. $V$ is non-empty since $3(0) + 4(0) + 5(0) = 0 \implies \mathbf{0} \in V$.
    <2>2. Let $\mathbf{u} = (u_1, u_2, u_3) \in V$, $\mathbf{v} = (v_1, v_2, v_3) \in V$, and $c \in \mathbb{R}$.
        Then $c\mathbf{u} + \mathbf{v} = (cu_1+v_1, cu_2+v_2, cu_3+v_3)$.
        Evaluating the defining condition:
        $$3(cu_1+v_1) + 4(cu_2+v_2) + 5(cu_3+v_3) = c(3u_1+4u_2+5u_3) + (3v_1+4v_2+5v_3) = c(0) + 0 = 0.$$
        Thus $c\mathbf{u} + \mathbf{v} \in V$. By the Subspace Criterion, $V \le \mathbb{R}^3$.

<1>2. $\dim(V) = 2$.
    Proof: $V$ is the kernel of the nonzero linear functional $\phi: \mathbb{R}^3 \to \mathbb{R}$, $\phi(x,y,z) = 3x+4y+5z$. Since $\operatorname{im}(\phi) = \mathbb{R}$ has dimension $1$, the Rank-Nullity Theorem yields $\dim(V) = \dim(\ker \phi) = 3 - 1 = 2$.
    A basis for $V$ is given by $\{v_1, v_2\}$ where $v_1 = (4, -3, 0)^T$ and $v_2 = (5, 0, -3)^T$.

<1>3. There exists a linear map $S: \mathbb{R}^3 \to \mathbb{R}^3$ with $\ker(S) = V$.
    Proof: Define $S$ via the matrix:
    $$S = \begin{pmatrix} 3 & 4 & 5 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
    For any $\mathbf{x} = (x,y,z)^T \in \mathbb{R}^3$, $S\mathbf{x} = (3x+4y+5z, 0, 0)^T$.
    Thus $S\mathbf{x} = \mathbf{0} \iff 3x+4y+5z = 0 \iff \mathbf{x} \in V$. Hence $\ker(S) = V$.

<1>4. There exists a linear map $T: \mathbb{R}^3 \to \mathbb{R}^3$ with $\operatorname{im}(T) = V$.
    Proof: By <1>2, $v_1 = (4, -3, 0)^T \in V$ and $v_2 = (5, 0, -3)^T \in V$ are linearly independent.
    Define $T: \mathbb{R}^3 \to \mathbb{R}^3$ by the matrix whose columns are $v_1, v_2, \mathbf{0}$:
    $$T = \begin{pmatrix} 4 & 5 & 0 \\ -3 & 0 & 0 \\ 0 & -3 & 0 \end{pmatrix}.$$
    The image of $T$ is the column space of $T$, which is $\operatorname{span}\{v_1, v_2\} = V$.

<1>5. There is NO linear map $U: \mathbb{R}^3 \to \mathbb{R}^3$ with $\ker(U) = \operatorname{im}(U) = V$.
    Proof:
    <2>1. By the Rank-Nullity Theorem, for any linear map $U: \mathbb{R}^3 \to \mathbb{R}^3$:
        $$\dim(\ker U) + \dim(\operatorname{im} U) = \dim(\mathbb{R}^3) = 3.$$
    <2>2. If $\ker(U) = \operatorname{im}(U) = V$, then by <1>2:
        $$\dim(\ker U) + \dim(\operatorname{im} U) = \dim(V) + \dim(V) = 2 + 2 = 4.$$
    <2>3. This contradicts <2>1 since $4 \neq 3$. Hence no such $U$ can exist. Q.E.D.
:::
