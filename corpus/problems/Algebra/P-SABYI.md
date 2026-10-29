---
schema: qual/card@1
id: P-SABYI
kind: problem
title: Structure theorem for finitely generated modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Principal Ideal Domains
  - Abelian Groups
relations: []
review: draft
---

::: {.problem}
State and explain a proof of the structure theorem for finitely generated modules over a PID. What are the module and the PID in the case of finitely generated abelian groups?
:::

::: {.solution}

Let $R$ be a PID and let $M$ be a finitely generated $R$-module.

::: pf

::: pf-step

Statement: there are a unique integer $r\ge0$ and nonzero nonunits $d_1\mid d_2\mid\cdots\mid d_s$, unique up to associates, such that
$$
M\cong R^r\oplus R/(d_1)\oplus\cdots\oplus R/(d_s).
$$
Equivalently, the torsion part decomposes into primary cyclic summands $R/(p^e)$.

:::

::: {.pf-step #presentation}

$M\cong\operatorname{coker}(A)$ for a matrix $A$ giving a map $R^m\to R^n$.

::: pf-proof

Generators $x_1,\ldots,x_n$ of $M$ give a surjection $R^n\twoheadrightarrow M$ with kernel $K$. Over a PID, a submodule of a finite free module is free of finite rank, so $K\cong R^m$, and the inclusion $K\hookrightarrow R^n$ is a matrix $A$ with $R^m\xrightarrow{A}R^n\to M\to0$ exact.

:::

:::

::: {.pf-step #existence}

Existence holds.

::: pf-proof

Over a PID, invertible row and column operations reduce $A$ to Smith normal form
$$
UAV=\operatorname{diag}(e_1,\ldots,e_t,0,\ldots,0),\qquad e_1\mid\cdots\mid e_t,\ e_i\neq0 .
$$
The invertible matrices $U,V$ change bases of $R^n$ and $R^m$, so they do not change the cokernel up to isomorphism. By step [](#presentation){.pf-ref}, $M\cong R^{n-t}\oplus\bigoplus_{i=1}^tR/(e_i)$. Discarding the $e_i$ that are units, which contribute $R/(e_i)=0$, gives the stated form.

:::

:::

::: pf-step

Uniqueness holds.

::: pf-proof

The rank $r$ is the dimension of $M\otimes_RF$ over the fraction field $F$ of $R$. The invariant factors are determined by the torsion submodule; for a prime $p$, the numbers $\dim_{R/(p)}\bigl(p^{k}M_{\mathrm{tors}}/p^{k+1}M_{\mathrm{tors}}\bigr)$ count the summands $R/(d_i)$ with $p^{k+1}\mid d_i$, and these counts recover each $d_i$ up to associates.

:::

:::

::: pf-qed

For finitely generated abelian groups, take $R=\ZZ$ and regard an abelian group $A$ as a $\ZZ$-module via $n\cdot a=a+\cdots+a$. The theorem becomes
$$
A\cong\ZZ^r\oplus\ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_s\ZZ,\qquad 1<d_1\mid\cdots\mid d_s .
$$

:::

:::

:::
