---
schema: qual/card@1
id: P-MAXAT-6-08
kind: problem
title: Maxim algebraic topology 6.8
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 8 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find the smallest k such that $\mathbb { C P } ^ { n }$ can be smoothly embedded in $\mathbb { R } ^ { 2 n + k }$
:::

::: {.solution}

As stated for arbitrary $n$, this is not a problem with a known closed-form
answer. The exact Euclidean embedding dimension of $\mathbb{CP}^n$ is a
classical embedding problem. The standard results give sharp answers for many
families and nontrivial intervals in the remaining cases.

For a positive integer $n$, write
\[
\alpha(n)
\]
for the number of $1$'s in the binary expansion of $n$, and define
\[
N(n)
\coloneqq
\min\left\{
N:
\mathbb{CP}^n
\text{ admits a smooth embedding into }\mathbb R^N
\right\}.
\]
Then the requested number is
\[
k_{\min}(n)=N(n)-2n.
\]

::: pf

::: {.pf-step #s1-1}

A classical nonembedding theorem gives
\[
N(n)
>
4n-2\alpha(n).
\]
Equivalently,
\[
N(n)
\ge
4n-2\alpha(n)+1.
\]


::: pf-proof

This is the Atiyah--Hirzebruch/Feder--Segal nonembedding theorem for complex
projective spaces. In the notation used here, it states that
\[
\mathbb{CP}^n
\not\hookrightarrow
\mathbb R^{,4n-2\alpha(n)}.
\]
See the embedding results surveyed in the standard projective-space
immersion literature, for example Feder--Segal,
*Immersions and embeddings of projective spaces*.

Since $N(n)$ is an integer, the strict inequality is equivalent to the
displayed integer lower bound.

:::

:::

::: {.pf-step #s1-2}

Mukherjee's embedding theorem gives
\[
N(n)
\le
4n-\alpha(n).
\]
If $n>1$ is odd, it improves to
\[
N(n)
\le
4n-\alpha(n)-1.
\]


::: pf-proof

These are the embeddings constructed by A. Mukherjee,
*Embedding complex projective spaces in Euclidean space*,
Bull. London Math. Soc. 13 (1981), 323--324.

:::

:::

::: {.pf-step #s1-3}

Hence for arbitrary $n$ one has
\[
\boxed{
2n-2\alpha(n)+1
\le
k_{\min}(n)
\le
2n-\alpha(n).
}
\]
For odd $n>1$,
\[
\boxed{
2n-2\alpha(n)+1
\le
k_{\min}(n)
\le
2n-\alpha(n)-1.
}
\]


::: pf-proof

Subtract the real dimension
\[
2n
\]
of $\mathbb{CP}^n$ from the lower bound in step [](#s1-1){.pf-ref} and the upper bounds in
step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

If
\[
\alpha(n)=1,
\]
equivalently
\[
n=2^r,
\]
then the bounds coincide and
\[
\boxed{
N(n)=4n-1,
\qquad
k_{\min}(n)=2n-1.
}
\]


::: pf-proof

When $\alpha(n)=1$, step [](#s1-1){.pf-ref} gives
\[
N(n)
\ge
4n-1.
\]
Step [](#s1-2){.pf-ref} gives
\[
N(n)
\le
4n-1.
\]
Thus equality holds.

For $n=1$, this is the familiar embedding
\[
\mathbb{CP}^1\cong S^2\hookrightarrow\mathbb R^3.
\]

:::

:::

::: {.pf-step #s1-5}

If $n>1$ is odd and
\[
\alpha(n)=2,
\]
then
\[
\boxed{
N(n)=4n-3,
\qquad
k_{\min}(n)=2n-3.
}
\]


::: pf-proof

Step [](#s1-1){.pf-ref} gives
\[
N(n)
>
4n-4,
\]
so
\[
N(n)\ge4n-3.
\]
Because $n$ is odd, the improved upper bound in step [](#s1-2){.pf-ref} gives
\[
N(n)
\le
4n-\alpha(n)-1
=
4n-3.
\]
Hence equality holds.

:::

:::

::: {.pf-step #s1-6}

If $n$ is even and
\[
\alpha(n)=2,
\]
then
\[
\boxed{
N(n)=4n-2,
\qquad
k_{\min}(n)=2n-2.
}
\]


::: pf-proof

Sanderson--Schwarzenberger's nonimmersion theorem implies in this case that
\[
\mathbb{CP}^n
\not\looparrowright
\mathbb R^{,4n-3}.
\]
In particular it cannot embed there, so
\[
N(n)\ge4n-2.
\]

Mukherjee's upper bound from step [](#s1-2){.pf-ref} gives
\[
N(n)
\le
4n-\alpha(n)
=
4n-2.
\]
Thus equality holds.

:::

:::

::: {.pf-step #s1-7}

The bounds do not coincide for all $n$; for example
\[
n=7
\]
gives only
\[
\boxed{
N(7)\in\{23,24\},
\qquad
k_{\min}(7)\in\{9,10\}
}
\]
from the established general results.


::: pf-proof

The binary expansion
\[
7=111_2
\]
has
\[
\alpha(7)=3.
\]
Step [](#s1-1){.pf-ref} gives
\[
N(7)>4\cdot7-2\cdot3=22,
\]
so
\[
N(7)\ge23.
\]
Since $7$ is odd, step [](#s1-2){.pf-ref} gives
\[
N(7)
\le
4\cdot7-3-1
=
24.
\]
Thus
\[
N(7)\in\{23,24\}.
\]
This same unresolved two-value range is recorded explicitly in the modern
embedding-dimension literature; see González--Landweber--Shimkus,
*On the embedding dimension of 2-torsion lens spaces*,
Homology Homotopy Appl. 11 (2009), §6.

:::

:::

::: pf-step

Consequently the literal request to “find the smallest $k$” for
arbitrary $n$ has no single presently established formula.


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} show that exact values are known in substantial families,
but step [](#s1-7){.pf-ref} exhibits a value of $n$ for which the cited general embedding
theorems leave two possibilities. Therefore replacing the bounds by one
uniform exact expression would assert a theorem stronger than the established
results used here.

:::

:::

::: pf-qed

The mathematically correct answer is therefore the invariant
\[
k_{\min}(n)=N(n)-2n
\]
with the bounds in step [](#s1-3){.pf-ref} and the exact special families in
steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}; the source problem is too strong as a request for a general
closed formula.

:::

:::

:::
