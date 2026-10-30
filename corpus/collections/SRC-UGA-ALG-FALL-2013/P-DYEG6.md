---
schema: qual/card@1
id: P-DYEG6
kind: problem
title: Separable extensions, separability over finite fields, and an inseparable finite
  extension
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Field Extensions
  - Finite Fields
relations: []
review: draft
---

::: {.problem}
Let $L/K$ be a finite extension of fields.

a.
Define what it means for $L/K$ to be *separable*.

b.
Show that if $K$ is a finite field, then $L/K$ is always separable.

c.
Give an example of a finite extension $L/K$ that is not separable.
:::

::: {.solution}

::: pf

::: {.pf-step #def}

$L/K$ is separable when the minimal polynomial over $K$ of every $\alpha\in L$ has distinct roots in an algebraic closure of $K$.

:::

::: {.pf-step #insep-form}

If $f\in K[x]$ is irreducible and has a repeated root, then $\operatorname{char}K=p>0$ and $f(x)=g(x^p)$ for some $g\in K[x]$.

::: pf-proof

A repeated root of $f$ is a common root of $f$ and $f'$, so $\gcd(f,f')\neq1$. Since $f$ is irreducible, $f\mid f'$, and $\deg f'<\deg f$ forces $f'=0$. If $f=\sum_k a_kx^k$, then $ka_k=0$ for all $k$. In characteristic $0$ this gives $f$ constant, which is impossible. In characteristic $p$ it gives $a_k=0$ unless $p\mid k$, so $f(x)=g(x^p)$ with $g(x)=\sum_j a_{jp}x^j$.

:::

:::

::: {.pf-step #finite}

If $K$ is finite, then every finite extension $L/K$ is separable.

::: pf-proof

Let $\operatorname{char}K=p$. The Frobenius map $c\mapsto c^p$ is an injective field homomorphism $K\to K$, so it is surjective because $K$ is finite. Suppose the minimal polynomial $f$ of some $\alpha\in L$ had a repeated root. By Step [](#insep-form){.pf-ref}, $f(x)=\sum_j a_jx^{jp}$. Choose $b_j\in K$ with $b_j^p=a_j$. Then
$$
f(x)=\sum_j b_j^p x^{jp}=\Bigl(\sum_j b_jx^j\Bigr)^p,
$$
because the $p$-th power map is additive in characteristic $p$. This contradicts the irreducibility of $f$.

:::

:::

::: {.pf-step #example}

The extension $L=\FF_p(s)\supset K=\FF_p(t)$ with $t=s^p$, where $s$ is transcendental over $\FF_p$, is finite and not separable.

::: pf-proof

$s$ is a root of $f(x)=x^p-t\in K[x]$. This polynomial is Eisenstein at the prime $t$ of $\FF_p[t]$, so it is irreducible over $\FF_p[t]$ and, by Gauss's lemma, over $K$. Hence $f$ is the minimal polynomial of $s$ and $[L:K]=p$. In $L[x]$, $f(x)=(x-s)^p$, so its only root $s$ has multiplicity $p$.

:::

:::

::: pf-qed

Steps [](#def){.pf-ref}, [](#finite){.pf-ref} and [](#example){.pf-ref} answer parts (a), (b) and (c).

:::

:::

:::
