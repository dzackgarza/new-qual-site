---
schema: qual/card@1
id: S-ZQPC5
kind: solution
title: Solution to P-HWAMG
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Counterexamples
relations:
- kind: solves
  target: P-HWAMG
review: draft
---

:::{.solution}
Define $\text{osc}_f(x)=\inf\{\sup_{z,y\in U}|f(z)-f(y)| : U \text{ is a nbhd of } x\}$. The set $\{x:\text{osc}_f(x)<t\}$ is open: if $\text{osc}_f(x)<t$, choose a nbhd $U$ of $x$ with $\sup_{z,y\in U}|f(z)-f(y)|<t$; then every $x'\in U$ also has $U$ as a nbhd, so $\text{osc}_f(x')\le\sup_{z,y\in U}|f(z)-f(y)|<t$. Also $f$ is continuous at $x$ iff $\text{osc}_f(x)=0$: continuity at $x$ says that for each $\eps>0$ there is a nbhd $U$ with $\abs{f(z)-f(x)}<\eps/2$ for $z\in U$, whence $\abs{f(z)-f(y)}\le\abs{f(z)-f(x)}+\abs{f(x)-f(y)}<\eps$ for $z,y\in U$ and $\text{osc}_f(x)\le\eps$; conversely $\text{osc}_f(x)=0$ gives for each $\eps>0$ a nbhd $U$ with $\abs{f(z)-f(x)}\le\sup_{z',y\in U}\abs{f(z')-f(y)}<\eps$. Hence $\{x:f \text{ is continuous at } x\}=\{x:\text{osc}_f(x)=0\}=\bigcap_{n=1}^\infty\{x:\text{osc}_f(x)<1/n\}$, a $G_\delta$ since each set in the intersection is open. It implies that $\{x:f\text{ is discontinuous at }x\}$ is a $F_\sigma$, i.e. a countable union of closed subsets.

For the second part, suppose there is a one. Then $\{x:f \text{ is continuous at } x\}=\mathbb{Q}$ is a dense $G_\delta$ set, say co-meager, which means that the set $Ir$ of all irrationals is meager. Since $\mathbb{Q}$ is also countable, thus meager, $[0,1]=\mathbb{Q}\bigsqcup Ir$ is also a meager set. A contradiction to the Baire category theorem.
:::
