---
schema: qual/card@1
id: P-UCTOP290-S9-3
kind: problem
title: Euler characteristic and Betti numbers under surface covers
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 9, Problem 3 in its checked-in extraction; its requested decrease of a homology rank under a finite cover is false.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 9, problem 3
    (assets/attachments/UCSD_290_F14_sheet9.pdf, printed page 266), from the
    checked-in extraction and a 300 dpi render. Part (a) asks to show that the
    orientable surface of genus 10 cannot be a covering space of the surface of
    genus 5. Part (b) as printed asks for examples showing that the ranks of
    individual homology groups do not satisfy a law like that of question 2(c)
    "and in fact may decrease as well as increase when we go up from X to Y".
    The second clause of (b) is false for a finite covering: the transfer shows
    dim H_i(Y;Q) >= dim H_i(X;Q) for every i. The card states part (b) as the
    question of how individual rational ranks can change and records the
    impossibility of a decrease in a remark, which is the repaired form; that
    repair was read against the printed clause here and stands.
---

::: {.problem}
Show that the genus-ten orientable surface
$\Sigma_{10}$ cannot cover $\Sigma_5$.
Determine how individual rational homology
ranks can change under a finite covering.
:::

::: {.solution}

Write $\Sigma_g$ for the closed orientable surface of genus $g$, so that
$\chi(\Sigma_g)=2-2g$.

::: pf

::: {.pf-step #sign}

$\chi(\Sigma_{10})=-18$ and $\chi(\Sigma_5)=-8$.

::: pf-proof

$\chi(\Sigma_g)=2-2g$, so $\chi(\Sigma_{10})=2-20=-18$ and
$\chi(\Sigma_5)=2-10=-8$.

:::

:::

::: {.pf-step #multiplicative}

If $p\colon Y\to X$ is a $d$-sheeted covering of finite CW complexes then
$\chi(Y)=d\,\chi(X)$; in particular a $d$-sheeted cover of $\Sigma_5$ has
Euler characteristic $-8d$.

::: pf-proof

Give $X$ a finite CW structure; its preimage under $p$ is a CW structure on
$Y$ with exactly $d$ cells over each cell of $X$, because $p$ is a local
homeomorphism and each open cell is evenly covered. Summing the alternating
cell counts with multiplicity $d$ gives $\chi(Y)=d\chi(X)$. This is question
2(c) of the same sheet.

:::

:::

::: {.pf-step #noten}

$\Sigma_{10}$ is not a covering space of $\Sigma_5$.

::: pf-proof

Suppose $p\colon\Sigma_{10}\to\Sigma_5$ were a $d$-sheeted covering. Steps
[](#sign){.pf-ref} and [](#multiplicative){.pf-ref} give $-18=-8d$, so
$d=18/8=9/4$, which is not an integer. Hence no such covering exists, whatever
the degree.

:::

:::

::: {.pf-step #transfer}

For a $d$-sheeted covering $p\colon Y\to X$ of path-connected spaces and every
$i$, $\dim_\QQ H_i(Y;\QQ)\ge\dim_\QQ H_i(X;\QQ)$.

::: pf-proof

The transfer $\tau\colon C_*(X;\QQ)\to C_*(Y;\QQ)$ sends a singular simplex
$\sigma$ to the sum of its $d$ lifts, and is a chain map with
$p_\#\tau=d\cdot\mathrm{id}$; on homology it gives $\tau_*\colon H_i(X;\QQ)\to
H_i(Y;\QQ)$ with $p_*\tau_*=d\cdot\mathrm{id}$. An endomorphism $\tau_*$ of
$H_i(X;\QQ)$ with $p_*\tau_*$ invertible makes $\tau_*$ injective, so $\dim
H_i(Y;\QQ)\ge\dim H_i(X;\QQ)$. Homology and cohomology have the same dimension
over the field $\QQ$ by the universal coefficient theorem.

:::

:::

::: {.pf-step #examples}

The individual ranks can grow by more than the degree, for instance
$b_1(\Sigma_3)=6>4=b_1(\Sigma_2)$ over a double cover, and can stay equal, as
for the finite covers of $S^1$; they cannot decrease, so the printed request
for an example in which one decreases has no answer.

::: pf-proof

A connected double cover of $\Sigma_2$ has Euler characteristic
$2\cdot(-2)=-4$, so it is $\Sigma_3$, and then $b_1(\Sigma_3)=6$ while
$b_1(\Sigma_2)=4$: the rank grows by $2$, not by the factor $2$, so no simple
multiplicativity holds for individual ranks. The $d$-sheeted covers of $S^1$
are again circles, with $b_1=1$ for every $d$. By step [](#transfer){.pf-ref}
a decrease is impossible for any finite covering, so the second clause of the
printed part (b) is false as printed; what can be said is that the ranks are
non-decreasing and that $\chi$ alone is multiplicative.

:::

:::

:::

::: {.remark}

The source asks for an example in which an individual rank decreases from the
base to the cover. Such an example cannot exist for a finite cover, by the
transfer argument of step [](#transfer){.pf-ref}; the printed clause is false
as it stands.

:::


:::
