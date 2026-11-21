---
schema: qual/card@1
id: P-APAS13E
kind: problem
title: Induced representations and Frobenius reciprocity
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Notation repair after the corpus check reported an undefined control word. The
    three occurrences of `\Ind_{H}^{G}`, in parts (a) and (c) and in the proof of (a), name a
    control word that neither vocabularies/macros.json nor the MathJax command set the site
    loads defines, so the page could not render it; all three now read
    `\operatorname{Ind}_{H}^{G}`, the operator spelling. Mathematics and wording unchanged.
---

::: {.problem}
Let $H$ be a subgroup of $G$ and $A\colon H\to\mathrm{GL}_n(\CC)$ be a representation of $H$.
Let $\chi^A\colon H\to\CC$ be the character of $A$.
Define $\chi^{\overline{A}}\colon G\to\CC$ by
$$
\chi^{\overline{A}}(\sigma)=
\begin{cases}
\chi^A(\sigma) & \text{if }\sigma\in H,\\
0 & \text{if }\sigma\in G\setminus H.
\end{cases}
$$

(a) Define the representation $A\uparrow_H^G$.

(b) Prove that
$$
\chi^{A\uparrow_H^G}=\frac{1}{\cardinality{H}}\sum_{\sigma\in G}\sigma\cdot\chi^{\overline{A}}\cdot\sigma^{-1}.
$$

(c) State and prove the Frobenius Reciprocity Theorem.
:::

::: {.solution}

No retained solution set covers this exercise: the three parts are set out as separate steps, with the character computation counted over the cosets and the reciprocity proved by the tensor-Hom adjunction rather than by comparing inner products.

Let $H\le G$ finite, $A:H\to\GL_{n}(\CC)$ with space $V$ and character $\chi^{A}$, and let $\chi^{\overline A}$ be $\chi^{A}$ on $H$ and $0$ off $H$.

::: pf

::: {.pf-step #define}
(a) $A\uparrow_{H}^{G}$ is the representation of $G$ on $\operatorname{Ind}_{H}^{G}V=\CC[G]\otimes_{\CC[H]}V$ with $g\cdot(x\otimes v)=(gx)\otimes v$.

::: pf-proof
$\CC[G]$ is a $(G,H)$-bimodule, so the tensor product over $\CC[H]$ carries a left $G$-action by multiplication on the first factor, and it is finite dimensional: choosing coset representatives $t_{1},\dots,t_{r}$ of $G/H$ gives $\CC[G]=\bigoplus_{i}t_{i}\CC[H]$ as right $\CC[H]$-modules, hence $\operatorname{Ind}_{H}^{G}V=\bigoplus_{i}t_{i}\otimes V\cong V^{\oplus r}$ as vector spaces.
:::

:::

::: {.pf-step #char-cosets}
$\chi^{A\uparrow}(g)=\sum_{i}\chi^{A}(t_{i}^{-1}gt_{i})$, where the $i$-th term is read as $0$ when $t_{i}^{-1}gt_{i}\notin H$.

::: pf-proof
On the direct sum decomposition $t_{i}\otimes V$, the operator $g$ sends $t_{i}\otimes v$ to $gt_{i}\otimes v=t_{j}\otimes(h v)$ when $gt_{i}=t_{j}h$ with $h\in H$; so it maps the $i$-th summand to the $j(i)$-th, and the trace is the sum over those $i$ with $j(i)=i$, where the induced map on $V$ is $v\mapsto hv$ with $h=t_{i}^{-1}gt_{i}$.
:::

:::

::: {.pf-step #char-formula}
(b) $\chi^{A\uparrow}(g)=\dfrac{1}{\cardinality{H}}\sum_{\sigma\in G}\chi^{\overline A}(\sigma^{-1}g\sigma)$.

::: pf-proof
Fix $g$ and $h\in H$; for $x\in G$ one has $(xh)^{-1}g(xh)=h^{-1}(x^{-1}gx)h$, which lies in $H$ exactly when $x^{-1}gx$ does, and then its trace-of-$A$ value is $\chi^{A}\big(h^{-1}(x^{-1}gx)h\big)=\chi^{A}(x^{-1}gx)$ since characters are constant on conjugacy classes of $H$. Hence as $x$ ranges over the coset $t_{i}H$, the value $\chi^{\overline A}(x^{-1}gx)$ is constantly $\chi^{A}(t_{i}^{-1}gt_{i})$ (or $0$), and each coset contributes $\cardinality{H}$ times that. Summing over the $r$ cosets and dividing by $\cardinality{H}$ gives exactly the sum of step [](#char-cosets){.pf-ref}.
:::

:::

::: {.pf-step #reciprocity}
(c) For a representation $W$ of $G$ with character $\chi^{B}$, $\dim\Hom_{G}\big(\operatorname{Ind}_{H}^{G}V,W\big)=\dim\Hom_{H}\big(V,\Res_{H}^{G}W\big)$, equivalently $\langle\chi^{A\uparrow},\chi^{B}\rangle_{G}=\langle\chi^{A},\restrictionof{\chi^{B}}{H}\rangle_{H}$.

::: pf-proof
Tensor-Hom adjunction for the ring extension $\CC[H]\subseteq\CC[G]$ gives a natural isomorphism $\Hom_{G}\big(\CC[G]\otimes_{\CC[H]}V,W\big)\cong\Hom_{H}\big(V,W\big)$, the $H$-module structure on the right being the restriction; and $\Hom_{G}(\CC[G],W)\cong W$ by evaluation at $1$, which is compatible with the $H$-action. Taking dimensions gives the stated equality of inner products, since $\dim\Hom_{G}(U,W)=\langle\chi^{U},\chi^{W}\rangle_{G}$ for finite groups.
:::

:::

::: {.pf-qed}
(a) is step [](#define){.pf-ref}, (b) is steps [](#char-cosets){.pf-ref} and [](#char-formula){.pf-ref}, (c) is step [](#reciprocity){.pf-ref}.
:::

:::

:::
