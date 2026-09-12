---
schema: qual/card@1
id: P-AZ2FY
kind: problem
title: "Small sets for a Radon measure via the Vitali covering lemma"
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Vitali Covering Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the JHU Fall 2017 Analysis Qualifying Exam appearance in the preserved packet. The extracted Hausdorff-content bound dropped the factor epsilon; the card restores the intended bound $\mathcal M^1(E_\varepsilon)<10\varepsilon$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

3. For a Radon measure $\mu ,$ with $\textstyle \int _ { \mathbb { R } ^ { n } } d \mu = C$ . Prove that for all $\epsilon > 0$ , there exists a set $E _ { \epsilon } \subset \mathbb { R } ^ { n }$ such that
\[
\mathcal M^1(E_\epsilon)
:=\inf_{E_\epsilon\subset\bigcup_i B_i}
\sum_i\operatorname{diam}(B_i)
<10\epsilon,
\]
and for any $x\notin E_\epsilon$ and $r>0$,

$$
\int _ { B _ { r } ( x ) } d \mu \leq \frac { C r } { \epsilon } .
$$

(Hint: use Vitali covering lemma.)

::: solution
<1>1. Define the exceptional set by failure of the desired ball estimate.
::: proof
Set
\[
E_\varepsilon
:=
\left\{x\in\mathbb R^n:
\text{there exists }r>0\text{ with }
\mu(B_r(x))>\frac{Cr}{\varepsilon}
\right\}.
\]
Then by definition, if $x\notin E_\varepsilon$, we have
\[
\mu(B_r(x))\le \frac{Cr}{\varepsilon}
\]
for every $r>0$.
:::

<1>2. Observe that every bad witnessing ball has small radius.
::: proof
If $x\in E_\varepsilon$ and $B_r(x)$ witnesses membership, then
\[
\frac{Cr}{\varepsilon}<\mu(B_r(x))\le\mu(\mathbb R^n)=C.
\]
If $C>0$, this implies
\[
r<\varepsilon.
\]
If $C=0$, the conclusion is trivial with $E_\varepsilon=\varnothing$.
Thus all witnessing radii are uniformly bounded.
:::

<1>3. Apply the Vitali $5r$ covering lemma.
::: proof
Consider the family of all witnessing balls
\[
\mathcal B
=\left\{B_r(x):x\in E_\varepsilon,
\ \mu(B_r(x))>\frac{Cr}{\varepsilon}\right\}.
\]
By the $5r$ covering lemma, there exists a countable pairwise disjoint subfamily
\[
B_{r_i}(x_i)
\]
such that
\[
E_\varepsilon\subseteq\bigcup_i B_{5r_i}(x_i).
\]
Since the selected balls are disjoint,
\[
\sum_i\mu(B_{r_i}(x_i))
\le \mu(\mathbb R^n)=C.
\]
But every selected ball is bad, so
\[
\mu(B_{r_i}(x_i))>\frac{Cr_i}{\varepsilon}.
\]
Therefore
\[
\sum_i r_i
<\frac{\varepsilon}{C}
\sum_i\mu(B_{r_i}(x_i))
\le\varepsilon.
\]
:::

<1>4. Estimate the Hausdorff $1$-content.
::: proof
The balls $B_{5r_i}(x_i)$ cover $E_\varepsilon$, and
\[
\operatorname{diam}(B_{5r_i}(x_i))=10r_i.
\]
Hence
\[
\mathcal M^1(E_\varepsilon)
\le\sum_i10r_i
<10\varepsilon.
\]
Together with Step 1, this gives the required exceptional set and ball estimate.
:::
:::
