---
schema: qual/card@1
id: P-MMAQ-FBNP7JLLPX
kind: problem
title: Groups of order 57
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 4 of the Algebra Preliminary Examination 2017 (University of
    Washington), printed p. 1 of the single-page paper retained at
    assets/attachments/UW-Algebra-Qual-2017.pdf, is the statement the card answers, and the
    paragraph at the head of the solution records that the paper prints no solutions, so the
    argument is the card's own. Checked: the statement against the paper's text layer at the page
    named; the solution read for the Sylow count forcing a normal subgroup of order 19, the
    semidirect product, and the single nonabelian action given by b a b^{-1} = a^7;
    `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering and the QED. Not
    checked: no retained solution set exists for this paper to compare the argument with, and no
    other card of the collection in this pass.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: n_19 divides 3 and is 1 mod 19,
    so it is 1 and the Sylow 19-subgroup is normal; N cap P = 1 since gcd(19,3) = 1, hence
    |NP| = 57 and G is the semidirect product. Aut(C_19) = (Z/19)^x is cyclic of order 18, so it has
    a unique subgroup of order 3 and the actions of C_3 on C_19 are the trivial one and one class of
    nontrivial ones, two nontrivial homomorphisms differing by inversion of the source. The
    exhibited relation is checked: 7^3 = 343 = 18*19 + 1, so 7 has order 3 mod 19, and the
    semidirect product with bab^{-1} = a^7 is nonabelian while C_19 x C_3 = C_57 is abelian. The
    card's answer, exactly two groups, is unchanged; the card says the argument is its own.
---

::: {.problem}
Classify all groups of order 57.
:::


::: {.solution}
Sylow forces the $19$-subgroup normal, so $G$ is a semidirect product $C_{19}\rtimes_\varphi C_3$, and such a group is determined by the image of $\varphi$ in $\operatorname{Aut}(C_{19})\cong C_{18}$, which has a unique subgroup of order $3$; so there are exactly two groups, the cyclic one and one nonabelian one, exhibited by the relation $bab^{-1}=a^7$. The argument is this card's own: Problem 4 of the Algebra Preliminary Examination 2017 (University of Washington), printed p. 1 of the single-page paper retained at `assets/attachments/UW-Algebra-Qual-2017.pdf`, is the statement answered here, and no retained solution set covers it.

::: pf

::: {.pf-step #sylow}
$n_{19}=1$, so the Sylow $19$-subgroup $N\cong C_{19}$ is normal in $G$.

::: pf-proof
By Sylow's theorem $n_{19}\equiv1\pmod{19}$ and $n_{19}\mid[G:N]=3$; the divisors of $3$ are $1$ and $3$, and of these only $1$ is $1\bmod 19$. So there is a unique Sylow $19$-subgroup, and it is normal because it is fixed by conjugation, conjugation carrying Sylow $19$-subgroups to Sylow $19$-subgroups. A group of order $19$ is cyclic.
:::

:::


::: {.pf-step #split}
For a Sylow $3$-subgroup $P$ one has $N\cap P=1$ and $NP=G$, so $G=N\rtimes P\cong C_{19}\rtimes_\varphi C_3$ for some $\varphi\colon C_3\to\operatorname{Aut}(C_{19})$.

::: pf-proof
$N\cap P$ is a subgroup of both; its order divides $\gcd(19,3)=1$, so $N\cap P=1$. Then $\abs{NP}=\abs N\abs P/\abs{N\cap P}=19\cdot3=57=\abs G$, so $NP=G$. With $N$ normal and $N\cap P=1$, the multiplication map $N\rtimes P\to G$, $(n,p)\mapsto np$, is an isomorphism: it is a bijection by the computation, and it is a homomorphism because $N$ is normal. The action of $P\cong C_3$ on $N$ by conjugation is a homomorphism $\varphi\colon C_3\to\operatorname{Aut}(C_{19})$.
:::

:::


::: {.pf-step #aut}
$\operatorname{Aut}(C_{19})\cong(\ZZ/19)^\times\cong C_{18}$, which has a unique subgroup of order $3$; hence there are at most two isomorphism classes, according as $\varphi$ is trivial or not.

::: pf-proof
An automorphism of $C_{19}$ is determined by the image of a generator, which must be another generator, so $\operatorname{Aut}(C_{19})$ is the multiplicative group $(\ZZ/19)^\times$, cyclic of order $18$; it has a unique subgroup of each order dividing $18$, in particular exactly one of order $3$. A homomorphism $\varphi\colon C_3\to C_{18}$ has image of order $1$ or $3$; the trivial image is one case, and in the other case the image is that unique subgroup of order $3$. Two nontrivial $\varphi,\varphi'$ differ by an automorphism of the source: the two isomorphisms $C_3\to$ (that subgroup) differ by inversion, which is an automorphism of $C_3$, and the resulting semidirect products are isomorphic (conjugating by an automorphism of the complement). So there is one semidirect product for the trivial action and one isomorphism class for the nontrivial action.
:::

:::


::: {.pf-step #trivial}
The trivial action gives $C_{19}\times C_3\cong C_{57}$.

::: pf-proof
If $\varphi$ is trivial the product is direct, and $C_{19}\times C_3$ is cyclic because $\gcd(19,3)=1$ (Chinese remainder theorem), of order $57$.
:::

:::


::: {.pf-step #nontrivial}
The nontrivial action gives the group $\langle a,b\mid a^{19}=b^3=1,\ bab^{-1}=a^7\rangle$, which is nonabelian.

::: pf-proof
Since $7^3=343=18\cdot19+1\equiv1\pmod{19}$ and $7\not\equiv1$, the class of $7$ has order $3$ in $(\ZZ/19)^\times$, so the map $b\mapsto(a\mapsto a^7)$ defines a homomorphism $C_3\to\operatorname{Aut}(C_{19})$ with image of order $3$, i.e. the nontrivial action. The presentation given is that semidirect product, of order $57$. It is nonabelian because $bab^{-1}=a^7\ne a$.
:::

:::


::: {.pf-step #distinct}
The two groups are not isomorphic, so there are exactly two groups of order $57$.

::: pf-proof
$C_{57}$ is abelian and the other is not, so they are non-isomorphic; by steps [](#aut){.pf-ref} to [](#nontrivial){.pf-ref} every group of order $57$ is one of the two.
:::

:::


::: {.pf-step #conclusion}
The groups of order $57$ are, up to isomorphism, $C_{57}$ and $C_{19}\rtimes C_3$ with the nontrivial action.

::: pf-proof
Steps [](#sylow){.pf-ref} and [](#split){.pf-ref} show every such group is a semidirect product of the two Sylow subgroups, step [](#aut){.pf-ref} that only two actions occur up to isomorphism, and steps [](#trivial){.pf-ref}, [](#nontrivial){.pf-ref} and [](#distinct){.pf-ref} exhibit the two and separate them.
:::

:::

:::
:::
