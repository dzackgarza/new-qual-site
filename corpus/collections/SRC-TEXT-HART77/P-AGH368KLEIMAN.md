---
schema: qual/card@1
id: P-AGH368KLEIMAN
kind: problem
title: Kleiman's theorem on enough locally free sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Invertible Sheaves
  - Locally Factorial Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts and the pole-divisor hint with the retained Hartshorne III.6.8 transcription. Checked section extension against Stacks Project Tag 01PW. The proof establishes the needed separation of local subrings of the function field, constructs a section neighborhood at every point, and produces finitely many invertible summands by quasi-compactness.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Prove the following theorem of Kleiman: if $X$ is a noetherian, integral, separated, locally factorial scheme, then every coherent sheaf on $X$ is a quotient of a locally free sheaf (of finite rank).

(a) First show that open sets of the form $X_s$, for various $s \in \Gamma(X, \mcl)$, and various invertible sheaves $\mcl$ on $X$, form a base for the topology of $X$.

(b) Now use (II, 5.14) to show that any coherent sheaf is a quotient of a finite direct sum $\bigoplus_i \mcl_i^{n_i}$ for various invertible sheaves $\mcl_i$ and various integers $n_i$.
:::

::: {.hint}
For (a), given a closed point $x \in X$ and an open neighborhood $U$ of $x$, to show there is an $\mcl, s$ such that $x \in X_s \subseteq U$, first reduce to the case that $Z=X-U$ is irreducible.
Then let $\zeta$ be the generic point of $Z$.
Let $f \in K(X)$ be a rational function with $f \in \mco_x$, $f \notin \mco_\zeta$.
Let $D=(f)_{\infty}$, and let $\mcl=\mcl(D)$, $s \in \Gamma(X, \mcl(D))$ correspond to $D$ (II, §6).
:::

::: {.solution}
Write $K=K(X)$ and view every local ring of the integral scheme $X$ as a subring of $K$.
For an invertible sheaf $L$ and section $s$, let $X_s$ be the open subset where $s$ is a local frame.
Local factoriality implies normality and makes every Weil divisor Cartier, by the [[D-5PQ5W|Cartier--Weil comparison]].

<1>1. If $x\notin\overline{\{z\}}$, then there is $f\in\OO_{X,x}$ with $f\notin\OO_{X,z}$.

::: {.proof}
Suppose instead that $\OO_{X,x}\subseteq\OO_{X,z}$ inside $K$.
The induced morphism $\Spec\OO_{X,z}\to\Spec\OO_{X,x}\to X$ agrees at the generic point with the canonical morphism $\Spec\OO_{X,z}\to X$.
They must agree everywhere: their equalizer is a closed subscheme because $X$ is separated, contains the generic point, and is therefore the whole reduced integral source, as in [[P-AGH242AGREEDENSE]].

The image of $\Spec\OO_{X,x}\to X$ consists of the generalizations of $x$.
This follows on an affine neighborhood $\Spec A$ from the correspondence between primes of $A_{\mathfrak p_x}$ and primes of $A$ contained in $\mathfrak p_x$.
Equality of the two morphisms would therefore make $z$ a generalization of $x$, meaning $x\in\overline{\{z\}}$, a contradiction.
The asserted noninclusion of local rings supplies $f$, which is necessarily nonzero.
:::

<1>2. For every point $x$ and every open neighborhood $U$, there is an effective Cartier divisor $D$ with $x\notin\supp D$ and $X\setminus U\subseteq\supp D$.

::: {.proof}
First suppose $Z=X\setminus U$ is irreducible and nonempty, with generic point $z$.
Step <1>1 gives $f\in\OO_{X,x}\setminus\OO_{X,z}$.
Define its pole divisor
$$
D=(f)_\infty=\sum_H\max\{0,-v_H(f)\}H,
$$
where $H$ ranges over prime divisors.
This is a finite effective Weil divisor [@Har10a, Lemma II.6.1], and is an effective Cartier divisor because $X$ is locally factorial [@Har10a, Proposition II.6.11].

No component of $D$ contains $x$: at a height-one point generalizing $x$, the regular germ $f\in\OO_{X,x}$ remains regular after localization and has nonnegative valuation.
On the other hand, $z$ belongs to $\supp D$.
Indeed, express $f$ as a relatively prime fraction in the UFD $\OO_{X,z}$.
Since $f$ is not in that ring, its denominator has an irreducible factor not cancelled by the numerator.
The corresponding height-one prime gives a codimension-one point of $X$ generalizing $z$, with negative valuation of $f$.
The closure of that point is a component of $D$ containing $z$.
As the support is closed, it contains all of $Z=\overline{\{z\}}$.

In general, $X\setminus U$ has finitely many irreducible components $Z_1,\ldots,Z_t$ because $X$ is noetherian.
Apply the preceding construction to each $Z_i$ and take the sum of the resulting effective Cartier divisors.
Their supports all avoid $x$, and their union contains $X\setminus U$, proving the assertion.
If the complement is empty, take $D=0$.
:::

<1>3. The opens in (a) form a basis.

::: {.proof}
Given $x\in U$, choose $D$ from step <1>2 and put $L=\OO_X(D)$.
The effective divisor gives a canonical global section $s$ of $L$, namely the rational function $1$ in $\OO_X(D)\subseteq K$.
If $a$ is a local equation for $D$, the frame of $L$ is $a^{-1}$ and the coefficient of $s$ in this frame is $a$.
Thus $s$ is a frame exactly away from $D$, and
$$
x\in X_s=X\setminus\supp D\subseteq U.
$$
Every point and neighborhood have such a refinement, proving the basis assertion, including at nonclosed points.
:::

<1>4. Every coherent sheaf $F$ is a quotient of a finite direct sum of invertible sheaves.

::: {.proof}
For each $x$, choose an affine neighborhood $U_x$ and a finite family of sections generating $F|_{U_x}$.
By step <1>3, choose $W_x=X_{s_x}\subseteq U_x$ containing $x$, with $s_x\in\Gamma(X,L_x)$ and $L_x$ invertible.
Quasi-compactness of $X$ gives a finite cover by such opens, which we label $W_i=X_{s_i}$ for $1\le i\le t$.
Let $a_{ij}\in\Gamma(W_i,F)$ be the restrictions of the finite generating families just chosen.

By the section-extension lemma [@Har10a, Lemma II.5.14], for each pair $(i,j)$ there are $m_{ij}\ge0$ and
$$
b_{ij}\in\Gamma(X,F\otimes L_i^{\otimes m_{ij}})
\quad\text{with}\quad
b_{ij}|_{W_i}=a_{ij}\otimes s_i^{\otimes m_{ij}}.
$$
The lemma applies because $X$ is noetherian and $F$ is quasi-coherent; it does not require $W_i$ to be affine.
Each $b_{ij}$ defines a morphism $L_i^{\otimes(-m_{ij})}\to F$.
On $W_i$, use $s_i$ to trivialize $L_i$; the image of the resulting frame is precisely $a_{ij}$.
Hence the sum of these maps is a surjection
$$
\boxed{\bigoplus_{i,j}L_i^{\otimes(-m_{ij})}\twoheadrightarrow F.}
$$
There are finitely many pairs, and the displayed source is locally free of finite rank.
This proves (b) and the theorem.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove (a), including the existence of the rational function used in the hint, and step <1>4 proves (b).
:::
:::
