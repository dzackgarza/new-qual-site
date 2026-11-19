---
schema: qual/card@1
id: P-APAS24F
kind: problem
title: Unitary structure and character of $\mathcal{L}(V,W)$ as a $G$-representation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 6 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p.
    6 of the paper's own numbered pages, is the statement the card answers, and the head of the solution
    names it; the file retained at assets/attachments/SP24_math_202_exam.pdf puts a cover page before
    those pages, so paper p. 6 is its page 7. Checked: the statement against the paper's text layer at
    the page named; unitarity of $\omega$ under $\langle S,T\rangle=\Tr S^*T$, and the character
    $\overline{\chi_V}\chi_W$; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering
    and the QED. Not checked: no retained solution set exists for this paper to compare the argument
    with, and no other card of the collection in this pass.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: the adjoint identity (ABC)* = C*B*A* used in the unitarity
    computation, the cyclicity of the trace by name, and the description of the isomorphism
    L(V,W) = W tensor V* including how the action becomes psi tensor phi*, which the prose had
    asserted as "under this identification, the action is psi tensor phi*". Not claimed: a
    retained solution set; the provenance names the examination paper. Statement, and the
    character chi_W(g) times the conjugate of chi_V(g), unchanged.
---

::: {.problem}
Let $(V,\varphi)$ and $(W,\psi)$ be finite-dimensional unitary representations of a finite group $G$.
Let $\mathcal{L}(V,W)=\{\text{linear }T\colon V\to W\}$ equipped with the scalar product $\langle S,T\rangle=\operatorname{Tr}(S^*T)$.
For $g\in G$ and $T\in\mathcal{L}(V,W)$, put
$$
\omega(g)T=\psi(g)\,T\,\varphi(g^{-1}).
$$
Show that $(\mathcal{L}(V,W),\omega)$ is a unitary representation of $G$.
Compute the character of $(\mathcal{L}(V,W),\omega)$ in terms of the characters of $(V,\varphi)$ and $(W,\psi)$, showing your calculations.
:::

::: {.solution}

The problem is Problem 6 of the Qualifier Exam in Applied Algebra of May 23, 2024, printed p. 6 of the paper's numbered pages — the retained file `assets/attachments/SP24_math_202_exam.pdf` puts a cover page before them.

No retained solution set covers this problem: the collection's `provenance` names the Spring 2024 applied-algebra examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $(V,\varphi)$ and $(W,\psi)$ are finite-dimensional unitary representations of a finite group $G$, $\mathcal L(V,W)$ carries the Hilbert–Schmidt inner product $\langle S,T\rangle=\operatorname{Tr}(S^*T)$, and $\omega(g)T=\psi(g)T\varphi(g^{-1})$.

::: pf

::: {.pf-step #representation}
$\omega$ is a representation: $\omega(gh)=\omega(g)\omega(h)$ and $\omega(e)=\mathrm{id}$.

::: pf-proof
For $T\in\mathcal L(V,W)$,
$$
\omega(gh)T=\psi(gh)T\varphi\bigl((gh)^{-1}\bigr)=\psi(g)\psi(h)T\varphi(h^{-1})\varphi(g^{-1})=\omega(g)\bigl(\omega(h)T\bigr),
$$
using that $\varphi,\psi$ are homomorphisms and $(gh)^{-1}=h^{-1}g^{-1}$; and $\omega(e)T=\psi(e)T\varphi(e)=T$.

:::

:::

::: {.pf-step #unitary}
$\langle\omega(g)S,\omega(g)T\rangle=\langle S,T\rangle$ for all $g$, so each $\omega(g)$ is unitary.

::: pf-proof
$\varphi(g)$ and $\psi(g)$ are unitary, so $\varphi(g^{-1})=\varphi(g)^{-1}=\varphi(g)^*$ and $\psi(g^{-1})=\psi(g)^*$. Then, with $(ABC)^*=C^*B^*A^*$,
$$
\langle\omega(g)S,\omega(g)T\rangle=\operatorname{Tr}\bigl(\varphi(g)S^*\psi(g)^*\psi(g)T\varphi(g)^{-1}\bigr)=\operatorname{Tr}\bigl(\varphi(g)S^*T\varphi(g)^{-1}\bigr)=\operatorname{Tr}(S^*T),
$$
the middle equality using $\psi(g)^*\psi(g)=\mathrm{id}$ and the last using the cyclicity of the trace.

:::

:::

::: {.pf-step #tensor}
Under the natural isomorphism $\mathcal L(V,W)\cong W\otimes V^*$, the action $\omega$ corresponds to $\psi\otimes\varphi^*$, where $\varphi^*$ is the contragredient of $\varphi$.

::: pf-proof
The isomorphism sends $T$ to $\sum_ie_i\otimes$ the functional $v\mapsto$ (the $e_i$-coordinate of $Tv$), for a basis $e_i$ of $W$; it is canonical for finite-dimensional spaces. Under it, $T\mapsto\psi(g)T\varphi(g^{-1})$ becomes $w\otimes\lambda\mapsto\psi(g)w\otimes\bigl(\lambda\circ\varphi(g^{-1})\bigr)$, which is exactly $\psi(g)\otimes\varphi^*(g)$ with $\varphi^*(g)\lambda=\lambda\circ\varphi(g)^{-1}$.

:::

:::

::: {.pf-step #character}
$\chi_\omega(g)=\chi_W(g)\overline{\chi_V(g)}$.

::: pf-proof
The character of a tensor product of representations is the product of the characters, so $\chi_\omega(g)=\chi_W(g)\chi_{\varphi^*}(g)$ by step [](#tensor){.pf-ref}. For a finite-dimensional representation, the character of the contragredient at $g$ is the trace of the transpose-inverse, which equals the trace of $\varphi(g)^{-1}$; and for a unitary representation $\varphi(g)^{-1}=\varphi(g)^*$, whose trace is $\overline{\operatorname{Tr}\varphi(g)}$. Hence $\chi_{\varphi^*}(g)=\chi_V(g^{-1})=\overline{\chi_V(g)}$, and the formula follows.

:::

:::

::: {.pf-step #conclusion}
$(\mathcal L(V,W),\omega)$ is a unitary representation of $G$ with character $\chi_W\overline{\chi_V}$.

::: pf-proof
Steps [](#representation){.pf-ref} and [](#unitary){.pf-ref} make it a unitary representation, and step [](#character){.pf-ref} computes its character.

:::

:::

:::
:::
