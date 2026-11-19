---
schema: qual/card@1
id: P-MMAQ-DNT3HIFV7M
kind: problem
title: A projective resolution of $k\simeq R/(x,y)$ over $R=k[x,y]$ and $\Tor_i^R((x,y),k)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 7 of the Algebra Preliminary Examination, Autumn 2016
    (University of Washington), printed p. 2 of the two-page paper retained at
    assets/attachments/UW-Algebra-Qual-2016.pdf, is the statement the card answers, and the
    paragraph at the head of the solution records that the paper prints no solutions, so the
    argument is the card's own. Checked: both parts, including the displayed maps phi and psi
    against the paper's text layer at the page named; the solution read for the term-by-term
    exactness and for the Tor computation that shows I is not flat; `qualc.authoring check` on the
    card. The card carries no `pf` block, so `tmp/lam.sh` does not apply to it and was not run. Not
    checked: no retained solution set exists for this paper to compare the argument with, and no
    other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R = k[x,y]$ where $k$ is a field, and let $I=(x,y)R$.

(a) Show that
$$
0\longrightarrow R\xrightarrow{\phi}R\oplus R\xrightarrow{\psi}R\longrightarrow k\longrightarrow 0,
$$
where $\phi(a) = (-ya,xa)$, $\psi((a,b)) = xa+yb$ for $a,b \in R$, is a projective resolution of the $R$-module $k \simeq R/I$.

(b) Show that $I$ is not a flat $R$-module by computing $\Tor_i^R(I,k)$
:::


::: {.solution}

The problem is Problem 7 of the Algebra Preliminary Examination, Autumn 2016 (University of Washington), printed p. 2 of the two-page paper retained at `assets/attachments/UW-Algebra-Qual-2016.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is exactness of the displayed sequence checked term by term, and the truncated resolution that computes $\Tor_1^R(I,k)\cong k$, which rules out flatness.

Write $\varepsilon:R\to k=R/(x,y)$ for the quotient map.

First consider
$$
0\longrightarrow R\xrightarrow{\phi}R^2\xrightarrow{\psi}R\xrightarrow{\varepsilon}k\longrightarrow0,
$$
with
$$
\phi(a)=(-ya,xa),\qquad \psi(a,b)=xa+yb.
$$
All three nonzero modules in the resolution are free, hence projective. We verify exactness.

The map $\phi$ is injective: if $(-ya,xa)=(0,0)$, then $xa=0$; since $R=k[x,y]$ is a domain and $x\neq0$, we get $a=0$.

Also $\psi\phi=0$, because
$$
\psi(-ya,xa)=-xya+yxa=0.
$$
Conversely, suppose $(a,b)\in\ker\psi$. Then
$$
xa=-yb.
$$
Since $x$ is prime in the UFD $k[x,y]$ and $x\nmid y$, we have $x\mid b$; write $b=xc$. Substituting gives $xa=-yxc$, hence $a=-yc$. Therefore
$$
(a,b)=(-yc,xc)=\phi(c),
$$
so $\ker\psi=\operatorname{im}\phi$.

Finally,
$$
\operatorname{im}\psi=(x,y)=I=\ker\varepsilon,
$$
and $\varepsilon$ is surjective. Thus the displayed complex is a projective resolution of $k$.

For the Tor computation of $I$, truncate the resolution at $I=\operatorname{im}\psi$:
$$
0\longrightarrow R\xrightarrow{\phi}R^2\xrightarrow{\psi}I\longrightarrow0.
$$
This is a free resolution of $I$. Tensoring with $k=R/I$ gives
$$
0\longrightarrow k\xrightarrow{\phi\otimes 1}k^2\longrightarrow0.
$$
Because $x$ and $y$ act as zero on $k$, the map $\phi\otimes1$ is the zero map. Hence
$$
\Tor_1^R(I,k)\cong k,
\qquad
\Tor_0^R(I,k)=I\otimes_Rk\cong k^2,
$$
and, since the resolution has length one,
$$
\Tor_i^R(I,k)=0\qquad(i\ge2).
$$
In particular $\Tor_1^R(I,k)\neq0$. A flat module has vanishing $\Tor_1$ against every module, so $I$ is not flat.
:::
