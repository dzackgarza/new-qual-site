---
schema: qual/card@1
id: P-XRTSC
kind: problem
title: Rank-nullity over division rings, and left inverses of rectangular matrices
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Free Modules
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
**Lemma**:
The rank-nullity theorem holds over division rings.

Proof:
A linear map $\phi: D^m \to D^n$ induces a short exact sequence:
$$
0 \to \ker \phi \to D^m \mapsvia{\phi} \im\phi \to 0
$$

But every module over a division ring is free; in particular, $\im \phi \leq D^n$ is a module over $D$ and is thus free.
So by a lemma in class, since the right-most term is a free module, this sequence splits and we have
$$
D^m \cong \ker \phi \oplus \im \phi
$$

and taking dimensions yields 
$$
m = \dim \ker(\phi) + \rank(\phi).
$$
$\qed$

1. $A \in M(n\times m, D)$ has a left inverse $B \iff \rank(A) = m$:

$\implies$:
Suppose toward the contrapositive that $\rank(A) < m$, so $A$ has at least one pair of linearly dependent columns.
So wlog write 
$$
A = [\vector a_1^t, \vector a_2^t, \cdots, \vector a_m^t]
$$ 
in block form with each $\vector a_i$ a column vector, and we can assume that $\vector a_1, \vector a_2$ are linearly dependent.

Now suppose such a left inverse $B$ were to exist. 
Write it in block form as 
$$
B =[\vector b_1, \vector b_2, \cdots, \vector b_n]^t,
$$ 
so each $\vector b_i$ is a row of $B$.

Now if $BA = I_m$ is to hold, noting that $(BA)_{ij} = \inner{\vector b_i}{\vector a_j}$, we must have

\begin{align*}
I_{1,1}  &= \inner{\vector b_1}{\vector a_1} = 1 \\
I_{1, 2} &= \inner{\vector b_1}{\vector a_2} = 0 \\
I_{1, 3} &= \inner{\vector b_1}{\vector a_3} = 0 \\
&\vdots \\
I_{2, 1} &= \inner{\vector b_2}{\vector a_1} = 0 \\
I_{2, 2} &= \inner{\vector b_2}{\vector a_2} = 1 \\
I_{2, 3} &= \inner{\vector b_2}{\vector a_3} = 0 \\
&\vdots
.\end{align*}


But the claim is that this can *not* happen if $\vector a_1, \vector a_2$ are linearly dependent.
To see why, note that the linear dependence supplies elements $d_1, d_2 \neq 0 \in D$ such that $d_1 \vector a_1 + d_2 \vector a_2 = \vector 0$. 
But then taking inner products against, e.g. $\vector b_1$ (that is, applying $\inner{\vector b_1}{\wait}$ to everything in sight), we obtain

\begin{align*}
d_1 \vector a_1 + d_2 \vector a_2 = \vector 0 \\
\implies \inner{\vector b_1}{d_1 \vector a_1} + \inner{\vector b_1}{d_2 \vector a_2} = \inner{\vector b_1}{\vector 0} = 0 \\
\implies d_1 \inner{\vector b_1}{\vector a_1} + d_2\inner{\vector b_1}{\vector a_2} = \inner{\vector b_1}{\vector 0} = 0 \\
\implies d_1 \inner{\vector b_1}{\vector a_1} + d_2\inner{\vector b_1}{\vector a_2}  = 0 \\
\implies d_1 + d_2\inner{\vector b_1}{\vector a_2}  = 0 \\
\implies \inner{\vector b_1}{\vector a_2} = -\frac{d_1}{d_2} \neq 0 
,\end{align*}

which contradicts $\inner{\vector b_1}{\vector a_2} = 0$ as required by the previous equations.


$\impliedby$:
Suppose $\rank(A) = m$, so $A$ has $m$ linearly independent columns -- note that this is *all* of its columns.

> Note: since row rank equals column rank, this also says that $A$ has $m$ linearly independent rows, so $n\geq m$.

Viewing $A$ as a representative of a map $\phi: D^m \to D^n$, we find that $\dim \im \phi = m \leq n$.
In particular, from the rank nullity theorem, we have 
$$
m = \dim \ker \phi + \rank(\phi) = \dim \ker \phi + m \implies \dim \ker \phi = 0.
$$
So $\ker A = \theset{\vector 0}$, and $A$ represents an injective map $f_A: D^m \to D^n$.

But any injective *set* map $f: S_1\to S_2$ has a left-inverse $g$ such that $g\circ f = \id_{S_1}$. 
So $f_A: D^m \to D^n$ *as a set map* has a left inverse $g_B: D^n \to D^m$ satisfying $g_B\circ f_A = \id_{D^m}$.
But then taking the matrix associated to $g_B$ yields a matrix $B \in M(m\times n, D)$ such that $BA = I_m$ as desired.
$\qed$

2. $A$ has a right inverse $B \iff \rank(A) = n$:

$\implies$:
By a similar argument, supposing that $\rank A < n$ but $AB = I_n$ for some $B$, we find that $A$ has at least two linearly dependent *rows* this time, say $\vector a_1, \vector a_2$, whereas we obtain a system of equations of the form $\inner{a_i}{\vector b_k} = \delta_{ik}$ where $\vector b_i$ are now the columns of $B$.

In a similar manner, the linear dependence forces, say, $\inner{\vector a_2}{\vector b_1} \neq 0$, which is a contradiction.

$\impliedby$:
By another similar argument, we find that $A$ represents a map $f_A: D^m \to D^n$, and since $\rank A = \dim \im A = n$, we find that $A$ represents a surjective map $f_A$.
Surjective set maps have *right* inverses, so there is some $g_B: D^n \to D^m$ such that $f_A \circ g_B = \id_{D^n}$, and when translated to matrices this yields $AB = I_{n}$.
$\qed$
:::

::: {.solution}
**Goal.** Let $D$ be a division ring and $A \in M(n\times m, D)$. Prove the rank-nullity theorem over $D$, and characterize when $A$ has a left or right inverse.

<1>1. Every $D$-module is free, and rank-nullity holds.
<2>1. A linear map $\phi: D^m \to D^n$ gives a short exact sequence $0 \to \ker\phi \to D^m \to \im\phi \to 0$.
::: {.proof}
exactness at each term is the definition of kernel and image.
:::
<2>2. $\im\phi \leq D^n$ is a submodule of a free module over a division ring, hence free.
::: {.proof}
every module over a division ring is free (a basis is a maximal linearly independent set).
:::
<2>3. The sequence splits, so $D^m \cong \ker\phi \oplus \im\phi$.
::: {.proof}
the rightmost term $\im\phi$ is free, hence projective, so the surjection $D^m \surjects \im\phi$ admits a section.
:::
<2>4. $m = \dim\ker\phi + \rank\phi$.
::: {.proof}
dimension is additive over direct sums, and $\rank\phi \definedas \dim\im\phi$.
:::

<1>2. $A$ has a left inverse $B$ (i.e. $BA = I_m$) iff $\rank A = m$.
<2>1. ($\Rightarrow$) If $\rank A < m$, some two columns of $A$ are linearly dependent.
::: {.proof}
$m$ columns spanning a space of dimension $< m$ are dependent.
:::
<2>2. Linear dependence of columns $\vector a_1, \vector a_2$ contradicts $BA = I_m$.
::: {.proof}
if $d_1\vector a_1 + d_2\vector a_2 = 0$ with $d_1, d_2 \neq 0$, then applying the first row $\vector b_1$ of $B$ gives $d_1 \inner{\vector b_1}{\vector a_1} + d_2 \inner{\vector b_1}{\vector a_2} = 0$; but $BA = I_m$ forces $\inner{\vector b_1}{\vector a_1} = 1$ and $\inner{\vector b_1}{\vector a_2} = 0$, so $d_1 = 0$, a contradiction.
:::
<2>3. ($\Leftarrow$) If $\rank A = m$, then $A$ is injective.
::: {.proof}
by <1>4, $m = \dim\ker\phi + m$, so $\ker\phi = 0$.
:::
<2>4. An injective map has a left inverse, giving $B$ with $BA = I_m$.
::: {.proof}
any injective set map $f: S_1 \to S_2$ admits $g: S_2 \to S_1$ with $g\circ f = \id_{S_1}$; the matrix of $g$ is $B$.
:::

<1>3. $A$ has a right inverse $B$ (i.e. $AB = I_n$) iff $\rank A = n$.
<2>1. ($\Rightarrow$) If $\rank A < n$, two rows of $A$ are linearly dependent, contradicting $AB = I_n$ by the row-analogue of <1>2.2.
<2>2. ($\Leftarrow$) If $\rank A = n$, then $A$ is surjective.
::: {.proof}
$\rank A = \dim\im A = n$ means $\im A = D^n$.
:::
<2>3. A surjective map has a right inverse, giving $B$ with $AB = I_n$.
::: {.proof}
any surjective set map $f: S_1 \to S_2$ admits $g: S_2 \to S_1$ with $f\circ g = \id_{S_2}$.
:::

<1>4. Q.E.D.
::: {.proof}
<1>2 and <1>3 are the two claimed equivalences.
:::
:::
