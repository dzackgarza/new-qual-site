---
schema: qual/card@1
id: E-HAT-3.B-2
kind: problem
title: "Chain homotopy as a chain map on the cone"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.B, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.B Exercise 2, printed p. 280; the statement
    matches the print, including the bracketed hint $h(c)=f(e\otimes c)$, and the differential
    formula $\partial(e\otimes c)=(v_1-v_0)\otimes c-e\otimes\partial c$ agrees with the Koszul sign
    rule applied to the degree-one element $e$. The converse direction, which the card had compressed
    into "the differential formulas show that $f$ commutes with $\partial$ on every summand", is now
    verified on both kinds of generators, and the mutual inverseness of the two constructions is
    stated; the degree count $(I\otimes C)_n=(I_0\otimes C_n)\oplus(I_1\otimes C_{n-1})$ and the fact
    that $h$ raises degree by one are now spelled out rather than left in a one-word proof. No
    published solution of this exercise is in the retained sets — Sam has no §3.B at all, Stanford
    215C solution2 covers only §3.B exercises 1 and 3, Li's contents stop at §3.3, and DeMason's
    chapter-three appendix appears nowhere in his table of contents — recorded in COMPLAINTS.md.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 2 of §3.B on printed p. 280,
    identical in the current online text, and the card states it word for word, including the
    bracketed hint $h(c)=f(e\otimes c)$. The obligation that #123 records is unchanged and stays
    open: no published solution of this exercise was located. Searched without result in the
    retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math
    205B help file, May, Bredon, Weibel's chapters 2--3 extracts, Maxim's Math 752 notes) and in
    Hatcher's text and errata.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The exercise now has a published proof, supplied by the owner for #123 and read in the text
    version: J. P. May, *A Concise Course in Algebraic Topology*, Chicago Lectures in Mathematics,
    University of Chicago Press 1999, Chapter 12 §3, the Lemma "A chain homotopy $s:f\simeq g$
    between chain maps $f,g:X\to X'$ determines and is determined by a chain map $h:X\otimes I\to
    X'$ such that $h(x,[0])=f(x)$ and $h(x,[1])=g(x)$", with its proof, on p. 92 of the revised PDF
    (page headed *A little homological algebra*, followed by p. 93, which opens §4). The solution is
    that lemma and proof transcribed in May's own convention $X\otimes I$ with $d[I]=[0]-[1]$ and
    the signed correspondence $(-1)^i s(x)=h(x\otimes[I])$, then transported to the exercise's
    convention $I\otimes C$ with $\partial e=v_1-v_0$ and the unsigned hint $h(c)=f(e\otimes c)$.
    The translation is stated on the card and proved there: the two copies of $I$ are the same
    complex under $[0]\mapsto v_1$, $[1]\mapsto v_0$, $[I]\mapsto e$, and May's $(-1)^i$ is the
    Koszul sign of the graded commutativity isomorphism $C\otimes I\to I\otimes C$, which cancels
    against it; consequently May's $f$ and $g$ are the exercise's $f_1$ and $f_0$. That is May's own
    closing sentence, "The sign in the correspondence would disappear if we replaced $X\otimes I$ by
    $I\otimes X$", on the same page. Not claimed: that May states or solves Hatcher's exercise; he
    states and proves the general lemma the exercise asks to be checked in one convention.
- event: solution-reviewed
  by: claude
  date: 2026-11-14
  note: >-
    Read the transcription against the source line by line. May's proof is one sentence — "the
    relation $d'_{i+1}(s_i(x))=f_i(x)-g_i(x)-s_{i-1}(d_i(x))$ corresponds to the relation $d'h=hd$
    by the definition of our differential on $I$" — and the card writes out both halves of that
    correspondence on the two kinds of generators, in May's convention: the degree-zero generators,
    where $d(x\otimes[j])=dx\otimes[j]$ and the chain-map property of $f$ and $g$ answers, and the
    degree-one generator, where $d(x\otimes[I])=dx\otimes[I]+(-1)^i x\otimes([0]-[1])$ and the
    identity $hd=d'h$ on it is exactly $d'_{i+1}s_i+s_{i-1}d_i=f_i-g_i$. Checked the converse
    direction and the mutual inverseness, which May states by the word "determines". Checked the
    translation by computing $F=h\circ\tau$ on each family: $\tau(e\otimes c)=(-1)^i c\otimes[I]$,
    so $F(e\otimes c)=(-1)^i(-1)^i s(c)=s(c)$, and $\tau(v_j\otimes c)=c\otimes v_j$ gives
    $F(v_1\otimes c)=f(c)$, $F(v_0\otimes c)=g(c)$. Checked the exercise's printed statement on
    Hatcher's p. 280, including the bracketed hint, which the boxed correspondence of the last step
    reproduces. Not verified: the pagination of the 1999 bound volume, which this machine does not
    hold; the page cited is the revised PDF's own printed page 92, as the card states.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Two errors in the transport between the two conventions are repaired. (1) The graded
    commutativity isomorphism was defined as $\tau:C\otimes I\to I\otimes C$ with
    $\tau(x\otimes y)=(-1)^{\deg x\deg y}y\otimes x$ and then applied in step 3 to elements $y\otimes x$
    of $I\otimes C$, where its inverse would be needed; it is now defined in that direction,
    $\tau:I\otimes C\to C\otimes I$ with $\tau(y\otimes x)=(-1)^{\deg x\deg y}x\otimes y$, so that
    $F=h\circ\tau$ is what step 3 forms. The values used there, $\tau(v_j\otimes c)=c\otimes v_j$ and
    $\tau(e\otimes c)=(-1)^i c\otimes[I]$, are unchanged. (2) The last step set $g=F_1$ and $f=F_0$
    before applying May's correspondence, which contradicts both the twist step — $F(v_1\otimes c)=f(c)$
    and $F(v_0\otimes c)=g(c)$ — and May's relation $\partial s+s\partial=f-g$ against the computed
    $\partial H+H\partial=F_1-F_0$; it now sets $f=F_1$, $g=F_0$, $s=H$, which is what the remark's
    "May's $f$ is the exercise's $f_1$" already said. The boxed correspondence no longer writes a
    direction $f_0\simeq f_1$ that the construction does not give, and states the two chain maps
    instead, as May's lemma does. Checked against May, *A Concise Course in Algebraic Topology*,
    Chapter 12 §3, the Lemma and its proof on printed p. 92 of the revised PDF: the correspondence
    $(-1)^i s(x)=h(x\otimes[I])$ with $h(x\otimes[0])=f(x)$, $h(x\otimes[1])=g(x)$, and the closing
    sentence that the sign disappears if $X\otimes I$ is replaced by $I\otimes X$. Checked the
    exercise's printed statement and bracketed hint on Hatcher (2002), §3.B Exercise 2, printed
    p. 280. Not claimed: a published solution of Hatcher's exercise as such.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Citations only; the statement and the proof are unchanged. Two defects. (1) No citation named its
    text version. May is read in `tmp/sources/may-concise-course-revised.md`, which was opened this
    pass and does contain the Lemma of Chapter 12 §3 at its line for the page headed *A little
    homological algebra*, and Hatcher in `tmp/sources/hatcher-2002-algebraic-topology.md`; both are
    now named in the remark under the solution. (2) The page reference "p. 92 of the revised PDF" could
    be read as PDF page 92, which it is not: the Lemma is on the page whose folio is 92, which is PDF
    page 100 of `tmp/sources/may-concise-course-revised.pdf` --- the front matter is unnumbered --- and
    the page before it, holding the start of Chapter 12, is PDF page 99 with folio 91, while the page
    after it is PDF page 101 with folio 93, opening §4. The remark now gives both numbers and says why
    they differ. Checked against Hatcher (2002), §3.B Exercise 2 on printed p. 280, with its bracketed
    hint $h(c)=f(e\otimes c)$. Not verified: the pagination of the 1999 bound volume, which this machine
    does not hold; nothing was read from a rendered page.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass: one citation defect, corrected on the card and in this record.
    The remark named `tmp/sources/may-concise-course-revised.pdf` as "the text version read here", which
    it is not: a PDF is not a text version, and the text version is
    `tmp/sources/may-concise-course-revised.md`, which the card did not name. The remark now names the
    `.md` and keeps the PDF only for the page, with folio 92, that both carry. The claim of the
    `source-corrected` note of this date that "both are now named in the remark under the solution" was
    therefore false for May, and is corrected here; Hatcher's
    `tmp/sources/hatcher-2002-algebraic-topology.md` was named there and still is. Checked in
    `tmp/sources/may-concise-course-revised.md`: the heading *A little homological algebra* opens
    Chapter 12 §3, and the Lemma "A chain homotopy $s:f\simeq g$ ... determines and is determined by a
    chain map $h:X\otimes\mathcal{I}\to X'$" with its one-sentence proof stands in that section, at
    the page whose folio is 92 (PDF page 100 of the PDF, the front matter being unnumbered). The
    statement and every step of the proof are unchanged.
---

::: {.problem}
Let $C$ and $C'$ be chain complexes, and let $I$ be the chain complex consisting of $\ZZ$ in dimension 1 and $\ZZ \times \ZZ$ in dimension 0, with the boundary map taking a generator $e$ in dimension 1 to the difference $v_1 - v_0$ of generators $v_i$ of the two $\ZZ$'s in dimension 0. Show that a chain map $f: I \otimes C \to C'$ is precisely the same as a chain homotopy between the two chain maps $f_i: C \to C'$, $c \mapsto f(v_i \otimes c)$, $i = 0, 1$.
[The chain homotopy is $h(c) = f(e \otimes c)$.]
:::

::: {.solution}

Throughout, chain complexes are of $\ZZ$-modules and their tensor product is graded with

$$
(C\otimes C')_n=\bigoplus_{i+j=n}C_i\otimes C'_j,
\qquad
d(x\otimes y)=dx\otimes y+(-1)^{i}x\otimes dy\quad (x\in C_i),
$$

the Koszul rule, which both sources use. Two copies of the two-term complex occur below. May's copy has generators $[0],[1]$ in degree $0$ and $[I]$ in degree $1$ with $d[I]=[0]-[1]$; the exercise's has generators $v_0,v_1$ in degree $0$ and $e$ in degree $1$ with $\partial e=v_1-v_0$. The assignment $\iota:[0]\mapsto v_1$, $[1]\mapsto v_0$, $[I]\mapsto e$ is an isomorphism of chain complexes, because it carries $d[I]=[0]-[1]$ to $v_1-v_0=\partial e$. May writes the tensor product $C\otimes I$ with his complex on the right, the exercise writes $I\otimes C$ with its complex on the left, and

$$
\tau:I\otimes C\longrightarrow C\otimes I,\qquad \tau(y\otimes x)=(-1)^{\gradeddegree{x}\gradeddegree{y}}x\otimes y,
$$

is the graded commutativity isomorphism, an isomorphism of chain complexes by the Koszul rule, and it runs from the exercise's convention into May's, which is the direction in which step [](#twist){.pf-ref} composes it with a chain map $C\otimes I\to C'$.

::: pf

::: {.pf-step #may-degree}

In May's convention, $C\otimes I$ has $(C\otimes I)_n=(C_n\otimes[0])\oplus(C_n\otimes[1])\oplus(C_{n-1}\otimes[I])$, and an additive map out of it is determined by its values on the three families $c\otimes[0]$, $c\otimes[1]$, $c\otimes[I]$.

::: pf-proof

$I_0=\ZZ[0]\oplus\ZZ[1]$ and $I_1=\ZZ[I]$, so $(C\otimes I)_n=(C_n\otimes I_0)\oplus(C_{n-1}\otimes I_1)$ is the direct sum displayed, and these summands are generated by the three families as $c$ ranges over a generating set of $C_n$, respectively $C_{n-1}$.

:::

:::

::: {.pf-step #may-sign}

In May's convention, the correspondence $s\leftrightarrow h$ given by $(-1)^{i}s(c)=h(c\otimes[I])$ for $c\in C_i$, together with $h(c\otimes[0])=f(c)$ and $h(c\otimes[1])=g(c)$, is a bijection between the chain homotopies $s:f\simeq g$ and the chain maps $h:C\otimes I\to C'$ with those two values.

::: pf-proof

Let $h$ be a chain map with the prescribed values on $c\otimes[0]$ and $c\otimes[1]$, and define $s$ by the displayed formula. On the degree-$0$ generators the chain-map condition is automatic: for $c\in C_i$ one has $d(c\otimes[j])=dc\otimes[j]$, since $d[j]=0$, so $hd(c\otimes[j])=f(dc)$ respectively $g(dc)$, while $d'h(c\otimes[j])=d'f(c)$ respectively $d'g(c)$, and the two agree because $f$ and $g$ are chain maps. On the degree-$1$ generator, $d(c\otimes[I])=dc\otimes[I]+(-1)^{i}c\otimes([0]-[1])$, so

$$
hd(c\otimes[I])=(-1)^{i-1}s(dc)+(-1)^{i}\bigl(f(c)-g(c)\bigr),
\qquad
d'h(c\otimes[I])=(-1)^{i}d's(c),
$$

and these are equal for every $c$ exactly when $d'_{i+1}s_i+s_{i-1}d_i=f_i-g_i$ for every $i$, which is the chain-homotopy relation. Conversely, given chain maps $f,g$ and a degree-one homomorphism $s$ satisfying that relation, the three formulas define an additive map $h$, and the same two computations, read backwards, show that $h$ is a chain map with the required values; step [](#may-degree){.pf-ref} says nothing further has to be checked. The two passages are inverse to each other.

:::

:::

::: {.pf-step #twist}

Transport by $\tau$ converts May's correspondence into the exercise's: if $h:C\otimes I\to C'$ is a chain map, then $F=h\circ\tau:I\otimes C\to C'$ is a chain map with $F(v_1\otimes c)=f(c)$, $F(v_0\otimes c)=g(c)$ and $F(e\otimes c)=s(c)$.

::: pf-proof

$\tau$ is an isomorphism of chain complexes, so $F=h\circ\tau$ is a chain map. On generators, $\tau(v_j\otimes c)=c\otimes v_j$, which is $c\otimes[0]$ for $j=1$ and $c\otimes[1]$ for $j=0$ under the identification $\iota$; hence $F(v_1\otimes c)=h(c\otimes[0])=f(c)$ and $F(v_0\otimes c)=h(c\otimes[1])=g(c)$. Since $e$ has degree $1$ and $c$ degree $i$, $\tau(e\otimes c)=(-1)^{i}c\otimes e=(-1)^{i}c\otimes[I]$, so $F(e\otimes c)=(-1)^{i}h(c\otimes[I])=(-1)^{i}(-1)^{i}s(c)=s(c)$: the two signs cancel, which is May's remark that the sign in his correspondence disappears when the tensor product is written with $I$ on the left.

:::

:::

::: {.pf-step #forward}

Conversely, let $F:I\otimes C\to C'$ be a chain map and put $F_i(c)=F(v_i\otimes c)$ and $H(c)=F(e\otimes c)$; then $F_0,F_1$ are chain maps and $H$ is a chain homotopy $F_1\simeq F_0$, that is $\partial H+H\partial=F_1-F_0$.

::: pf-proof

In the exercise's convention $(I\otimes C)_n=(v_0\otimes C_n)\oplus(v_1\otimes C_n)\oplus(e\otimes C_{n-1})$, with $\partial(v_i\otimes c)=v_i\otimes\partial c$ and $\partial(e\otimes c)=(v_1-v_0)\otimes c-e\otimes\partial c$. On $v_i\otimes c$ the chain-map condition reads $F_i(\partial c)=F(v_i\otimes\partial c)=F\partial(v_i\otimes c)=\partial F(v_i\otimes c)=\partial F_i(c)$. On $e\otimes c$, $F\partial(e\otimes c)=F_1(c)-F_0(c)-H(\partial c)$ and $\partial F(e\otimes c)=\partial H(c)$, so the chain-map condition is $\partial H+H\partial=F_1-F_0$. $H$ raises degree by one because $e$ does.

:::

:::

::: {.pf-step #inverse}

The two passages are mutually inverse, so chain maps $I\otimes C\to C'$ correspond bijectively to chain homotopies between chain maps $C\to C'$.

::: pf-proof

Starting from $F$, take $(F_0,F_1,H)$ as in step [](#forward){.pf-ref}, then let $f=F_1$, $g=F_0$ and $s=H$ and apply the construction of step [](#may-sign){.pf-ref}: this is the reading that matches the two conventions, since May's relation $\partial s+s\partial=f-g$ is $\partial H+H\partial=F_1-F_0$ here, and step [](#twist){.pf-ref} gives $F(v_1\otimes c)=f(c)$ and $F(v_0\otimes c)=g(c)$, so the resulting chain map agrees with $F$ on $v_i\otimes c$ and on $e\otimes c$, hence is $F$ by step [](#may-degree){.pf-ref} applied through $\tau$. Starting from $(f,g,s)$ the two steps produce the same values, so the composite is the identity. Step [](#twist){.pf-ref} is the dictionary between the two conventions, and it is a bijection on chain maps.

:::

:::

::: pf-step

A chain map $f:I\otimes C\to C'$ is precisely the same as a chain homotopy between the two chain maps $f_i:C\to C'$, $c\mapsto f(v_i\otimes c)$; the chain homotopy is $h(c)=f(e\otimes c)$, and this is May's lemma in the exercise's convention.

::: pf-proof

Steps [](#may-sign){.pf-ref}, [](#twist){.pf-ref}, [](#forward){.pf-ref} and [](#inverse){.pf-ref} give the bijection, in the two conventions, with the correspondence $h(c)=f(e\otimes c)$ of the exercise's hint, and

$$
\boxed{\{\text{chain maps }I\otimes C\to C'\}\ \cong\ \{\text{chain homotopies between the chain maps } f_0,f_1:C\to C'\}.}
$$

:::

:::

:::

:::

::: {.remark title="Source"}

The exercise is Exercise 2 of §3.B, printed p. 280, read in `tmp/sources/hatcher-2002-algebraic-topology.md`. The proof above is transcribed from **J. P. May, *A Concise Course in Algebraic Topology*, Chicago Lectures in Mathematics, University of Chicago Press 1999**, Chapter 12 §3 ("Tensor products of chain complexes"), the Lemma stating that a chain homotopy $s:f\simeq g$ determines and is determined by a chain map $h:X\otimes I\to X'$ with $h(x\otimes[0])=f(x)$ and $h(x\otimes[1])=g(x)$, with its proof, on the page of the revised PDF whose folio is **92** --- PDF page **100** of `tmp/sources/may-concise-course-revised.pdf` --- and the text version read here is `tmp/sources/may-concise-course-revised.md`, whose section *A little homological algebra* carries the Lemma --- the page headed *A little homological algebra*, followed by the page whose folio is 93, which opens §4. The differential $d(x\otimes y)=d(x)\otimes y+(-1)^{i}x\otimes d(y)$ and the complex $I$ with $d[I]=[0]-[1]$ are displayed immediately above the Lemma on the same page; the proof's closing sentence, that the sign in the correspondence disappears if $X\otimes I$ is replaced by $I\otimes X$, is on that page and is the translation step [](#twist){.pf-ref}. Pagination is that of the revised PDF's own printed folios, not of the 1999 bound volume; the folio and the PDF page number differ because the front matter is unpaginated.

The translation, stated: May's $I$ and the exercise's $I$ are the same two-term complex under $[0]\mapsto v_1$, $[1]\mapsto v_0$, $[I]\mapsto e$, which reverses the labels because May's differential is $[0]-[1]$ and the exercise's is $v_1-v_0$; and May's correspondence carries the factor $(-1)^{i}$ while the exercise's hint $h(c)=f(e\otimes c)$ carries none, because May places $I$ on the right of the tensor product and the graded commutativity isomorphism $\tau$ contributes $(-1)^{i}$ in moving the degree-one generator to the other side. Step [](#twist){.pf-ref} computes that the two signs cancel, so the exercise's correspondence is May's, with the two chain maps read in the opposite order: May's $f$ is the exercise's $f_1$ and May's $g$ is the exercise's $f_0$. Nothing in the proof depends on which of the two chain maps is called $f$ and which $g$, which is why the exercise can name them by the index $i$ alone.

:::
