---
schema: qual/card@1
id: P-AGH3118VANISHNBHD
kind: problem
title: Vanishing on one fibre forces a higher direct image to vanish nearby
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Higher Direct Images
  - Semicontinuity
  - Flat Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.8 in its source position at the end of the theorem-on-formal-functions section.
    The proof was written independently and then compared with an external solution transcription; both
    use flatness to pass vanishing through the infinitesimal neighbourhoods of the fibre. The formal-functions,
    coherence, and completion-plus-Nakayama steps were cross-checked against Stacks Project Tags 02OC,
    02O3, and 02OE.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $f: X \to Y$ be a projective morphism, let $\mcf$ be a coherent sheaf on $X$ which is flat over $Y$, and assume that $H^i(X_y, \mcf_y) = 0$ for some $i$ and some $y \in Y$.
Show that $R^i f_*(\mcf)$ is $0$ in a neighborhood of $y$.
:::

::: {.solution}
Under the standing Noetherian hypotheses of Hartshorne III.11, put
$$
A=\mco_{Y,y},
\qquad
\mfm=\mfm_y,
\qquad
k=\kappa(y).
$$
For $n\ge1$, let
$$
X_n=X\times_Y\Spec(A/\mfm^n)
$$
and let $\mcf_n$ be the pullback of $\mcf$ to $X_n$. Thus
$$
X_1=X_y,
\qquad
\mcf_1=\mcf_y.
$$

<1>1. For every $n\ge1$ there is a short exact sequence
$$
0
\longrightarrow
\mcf_y\otimes_k \mfm^n/\mfm^{n+1}
\longrightarrow
\mcf_{n+1}
\longrightarrow
\mcf_n
\longrightarrow0,
$$
where the first term is regarded as a sheaf on $X_{n+1}$ supported on
$X_y$.

::: {.proof}
Base-change first to $X_A=X\times_Y\Spec A$ and write $\mcf_A$ for the
pullback of $\mcf$. Flatness of $\mcf$ over $Y$ says that $\mcf_A$ is
flat over $A$. Hence tensoring the exact sequence
$$
0
\longrightarrow
\mfm^n/\mfm^{n+1}
\longrightarrow
A/\mfm^{n+1}
\longrightarrow
A/\mfm^n
\longrightarrow0
$$
with $\mcf_A$ remains exact. The middle and right terms are
$\mcf_{n+1}$ and $\mcf_n$. Since $\mfm$ annihilates
$\mfm^n/\mfm^{n+1}$, the left term is
$$
\mcf_y\otimes_k \mfm^n/\mfm^{n+1}.
$$
:::

<1>2. For every $n\ge1$,
$$
H^i(X_n,\mcf_n)=0.
$$

::: {.proof}
The case $n=1$ is the hypothesis
$$
H^i(X_y,\mcf_y)=0.
$$
Assume inductively that $H^i(X_n,\mcf_n)=0$. Because $A$ is Noetherian,
$\mfm^n/\mfm^{n+1}$ is a finite-dimensional $k$-vector space. Hence
$$
\mcf_y\otimes_k\mfm^n/\mfm^{n+1}
$$
is the pushforward from the closed fibre of a finite direct sum of copies
of $\mcf_y$. A closed immersion has exact pushforward, so its $i$-th
cohomology is the corresponding finite direct sum of
$H^i(X_y,\mcf_y)$ and is therefore zero. The long exact cohomology
sequence of step <1>1 consequently contains
an injection
$$
H^i(X_{n+1},\mcf_{n+1})
\hookrightarrow
H^i(X_n,\mcf_n)=0.
$$
Thus $H^i(X_{n+1},\mcf_{n+1})=0$, and induction proves the claim.
:::

<1>3. The completed stalk of $R^if_*\mcf$ at $y$ is zero:
$$
\widehat{(R^if_*\mcf)_y}=0.
$$

::: {.proof}
Since $f$ is projective, it is proper. By
[[T-COHFF|the theorem on formal functions]],
$$
\widehat{(R^if_*\mcf)_y}
\cong
\varprojlim_n H^i(X_n,\mcf_n).
$$
Every term of this inverse system is zero by step <1>2, so the inverse
limit is zero.
:::

<1>4. The stalk $(R^if_*\mcf)_y$ is zero.

::: {.proof}
For a projective morphism of Noetherian schemes, the higher direct image of
a coherent sheaf is coherent. Hence
$$
M=(R^if_*\mcf)_y
$$
is a finite $A$-module. Its $\mfm$-adic completion is zero by step <1>3.
Since
$$
\widehat M=\varprojlim_n M/\mfm^nM
$$
projects surjectively onto $M/\mfm M$, it follows that
$$
M/\mfm M=0.
$$
By [[T-DEFNAKA|Nakayama's lemma]], $M=0$.
:::

<1>5. There is an open neighborhood $U$ of $y$ such that
$$
R^if_*\mcf|_U=0.
$$

::: {.proof}
The sheaf $R^if_*\mcf$ is coherent. Its support is therefore closed. By
step <1>4, the point $y$ does not belong to this support, so the complement
of the support is an open neighborhood $U$ of $y$ on which the sheaf
vanishes.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is exactly the required neighborhood vanishing of
$R^if_*\mcf$.
:::
:::
