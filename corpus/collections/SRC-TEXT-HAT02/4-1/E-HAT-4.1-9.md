---
schema: qual/card@1
id: E-HAT-4.1-9
kind: problem
title: "Extending the long exact sequence to $\\pi_0$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher Section 4.1 Exercise 9 and the 2021-06-02 correction; corrected i^* to i_* in the stored statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct in its two parts. The extension by `pi_0(X,A,x_0) = pi_0(X,x_0) /
    i_* pi_0(A,x_0)` is exact at the tail because the components of `X` mapping to the distinguished
    relative class are precisely those meeting `A`, and the quotient map is onto. (a) The five-lemma in
    degrees `>= 2` is the ordinary one; in the pointed-set tail the argument is the appropriate
    replacement — exactness says that the fiber of the next map over the distinguished element is the
    image of the preceding map — and the hypothesis that the four surrounding maps are bijections *for all
    basepoints* is exactly what allows rebasing at an arbitrary component, which is the one place the
    naive group-theoretic version fails. (b) The triple sequence stops at `pi_0(A,B,x_0)` because there is
    no distinguished element of `pi_0(B)` to feed the next term. No correction was needed.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The printed part (a) is not correct as stated, and the earlier note's claim that "the hypothesis
    that the four surrounding maps are bijections for all basepoints is exactly what allows rebasing"
    does not repair it: rebasing is not available, because the basepoint of the pair $(Y,B)$ must lie
    in $B$ while the component of $B$ whose surjectivity is in question need not meet the image of
    $A$. Counterexample on the card: $X$ the disjoint union of a point $x_0$ and a point $a$ with
    $A=\{x_0,a\}$, $Y$ the disjoint union of a point $y_0$ and the interval $[0,1]$ with
    $B=\{y_0,0,1\}$, and $\varphi(x_0)=y_0$, $\varphi(a)=0$. Then the vertical maps at
    $\pi_1(X,A,x_0)$, $\pi_1(X,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$ are all bijections of
    one-point or two-point sets, while $\pi_0(A,x_0)\to\pi_0(B,y_0)$ is 2 points into 3 and is not
    onto. The card now states the exercise as printed and proves what is true: the five-lemma at
    every term in degrees $\ge1$ (both chases written out), the bijectivity of the vertical at
    $\pi_0(X,A,x_0)$ from those at $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$, and the surjectivity at
    $\pi_0(A,x_0)$ for the components of $B$ lying in the component of $y_0$ in $Y$. Part (b) is
    correct as printed and its example is checked point by point.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Read Hatcher's published errata list for *Algebraic Topology*
    (pi.math.cornell.edu/~hatcher/AT/ATerrata.pdf) for this exercise, as #123 asks. The only entry
    bearing on it is "§4.1, page 358, Exercise 9, first line. To avoid an abuse of notation, replace
    $\pi_0(A,x_0)$ by $i_*(\pi_0(A,x_0))$. (The previous version of this correction mistakenly said
    $i^*$ instead of the correct $i_*$.)" That is a notational correction of the displayed term and
    changes no hypothesis. The current online text of the book (AT.pdf, printed p. 358) carries it
    and is otherwise identical to the 2002 printing: part (a) still concludes that one of the maps
    is a bijection "if the four surrounding maps are bijections for all choices of $x_0$". So the
    errata supplies no corrected statement and does not repair the failure at the $\pi_0(A,x_0)$
    term; the counterexample on this card survives the corrected notation, since
    $i_*\pi_0(A,x_0)$ is the whole of $\pi_0(X,x_0)$ in it. The repaired statement proved above
    therefore stands as the card's own. Not established here: a published proof of that repaired
    statement. Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford
    Math 215C Solution Sets 1--5, the UCR Math 205B help file, May's *Concise Course* §4, Maxim's
    Math 752 notes) and in Hatcher's text and errata.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Withdraws the counterexample recorded on 2026-11-07, which does not satisfy the hypothesis it is
    offered against. That hypothesis is that the four surrounding maps are bijections for every
    choice of basepoint, and the basepoints admissible for the pair $(X,A,x_0)$ are the points of
    $A$. In the withdrawn example $X=\{x_0\}\sqcup\{a\}$ is discrete with $A=X$, while
    $Y=\{y_0\}\sqcup[0,1]$ and $B=\{y_0,0,1\}$; at the basepoint $a\in A$ the vertical map at
    $\pi_1(X,A,a)$ is one point into two, since the only path from $A$ to $a$ in the discrete $X$ is
    the constant one, while $\pi_1(Y,B,\varphi(a))=\pi_1(Y,B,0)$ contains the classes of the constant
    path at $0$ and of a path from $1$ to $0$, both starting in $B$. The example therefore fails the
    hypothesis at a basepoint in $A$, exactly as the brief for #123 asked to be checked, and it is
    withdrawn. It is replaced by two examples that do satisfy the hypothesis at every basepoint: for
    the term $\pi_1(X,A,x_0)$, $X=\RR\sqcup\RR$ with $A=\{1\}\cup\{2\}$ one point in each copy,
    $Y=\RR$ with $B=\{0,3\}$, and $\varphi$ equal to $0$ on the first copy and $3$ on the second; and
    for the term $\pi_0(A,x_0)$, $X=Y=\RR$ with $A=(-1,0]\cup(2,3)$, $B=(-1,1)$ and the piecewise map
    that is the identity on $(-\infty,0]$, $0$ on $[0,2]$ and $t-2$ on $[2,\infty)$. In each case the
    four surrounding maps are computed on the card, at every basepoint, and the conclusion fails.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Corrects the claim, carried since 2026-11-07, that the printed five-lemma holds "at every term in
    degrees $\ge1$". The group chase on the card is a chase of five group terms, and in the pair
    sequence the windows of five group terms are exactly those centered at a term of degree $\ge2$;
    the window centered at the pointed set $\pi_1(X,A,x_0)$ is not one of them, and the first new
    example shows that the printed claim is false there too. So the printed (a) fails at two terms,
    $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, and the card now says so. What survives is stated as Claim 1
    ($\pi_0(X,A,x_0)$ from $\pi_0(A,x_0)$ and $\pi_0(X,x_0)$), Claim 2 (unchanged), and a new Claim 3:
    surjectivity at $\pi_0(A,x_0)$ is forced by the hypothesis, using $\pi_1(X,A,x)$ onto at the
    relevant basepoints and $\pi_0(X,A,x_0)$ injective, so the failure at $\pi_0(A,x_0)$ is
    injectivity only and not, as the withdrawn example suggested, surjectivity. The windows centered
    at $\pi_1(A,x_0)$ and $\pi_1(X,x_0)$ are recorded on the card as not settled there. Part (b) is
    unchanged and still checked as printed.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    Read Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970) 103--132, in the text
    version `tmp/sources/brown-1970-fibrations-of-groupoids.md`, for the $\pi_0$ five-lemma the #123
    brief names: Theorem 4.9 on printed p. 121, whose (a) gives surjectivity of $f:\pi_0F\to\pi_0F'$
    from surjectivity of $h:H(v)\to H'(v')$ and of $g:\pi_0G\to\pi_0G'$ together with injectivity of
    $h:\pi_0H\to\pi_0H'$, and whose (b) gives injectivity of $f$ on $\ker(\pi_0F\to\pi_0G)$; and
    Corollary 4.11 on printed pp. 122--123, that equivalences $h:H\to H'$ and $g:G\to G'$ force
    $f:F\to F'$ to be an equivalence, hence $f:\pi_0F\to\pi_0F'$ bijective, by 4.9 followed by the
    ordinary five-lemma for groups on diagram 4.8. Cited on the card in a remark for exactly that,
    and not used in the argument: Brown's hypotheses are those of a fibration of groupoids with
    equivalences of the total groupoids and bases, which is stronger than the exercise's "for all
    choices of $x_0$", and the map of pairs $(X,A)\to(Y,B)$ is not a fibration of groupoids. No
    claim is made that Brown's theorem settles Hatcher's exercise. The extracted text of the paper
    writes some symbols as glyph substitutions (it is a scan of the 1970 print); the statements
    above were read against the displayed formulas of 4.9, 4.10 and 4.11, not from the running text
    alone.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    Withdraws the two counterexamples added earlier today and the claim they supported, that the
    printed (a) fails at the terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$. Both are disputed and neither
    is established. Against the first ($X=\RR\sqcup\RR$ with $A=\{1\}\cup\{2\}$, $Y=\RR$ with
    $B=\{0,3\}$): its vertical map $\pi_0(X)\to\pi_0(Y)$ is two components into one. Against the
    second ($X=Y=\RR$, $A=(-1,0]\cup(2,3)$, $B=(-1,1)$): $\pi_1(X,A,x_0)$ is read as having one class
    per component of $A$ rather than one per point of $A$, and then it is the surrounding map at
    $\pi_1(X,A,x_0)$ that fails rather than the one at $\pi_0(A,x_0)$. The second objection is about
    the definition of $\pi_1$ of a pointed pair, not about an example, so this reading is established
    neither on the card nor in prose: the question goes to a Lean declaration at
    <https://github.com/dzackgarza/lean-categories/issues/156>. The card now states the question as
    open at those two terms and asserts neither direction. The withdrawal of the 2026-11-07 example
    and the reason for it stand unchanged, and Claims 1, 2 and 3 stand: Claim 3 uses only that the
    map at $\pi_1(X,A,x)$ is onto at the relevant basepoints, so it holds under either reading of
    that set. Not claimed: that the printed (a) is correct, or that it is false; not verified: the
    contested reading of $\pi_1(X,A,x_0)$, which is what the issue is for.
---

::: {.problem}
Suppose we define $\pi_0(X, A, x_0)$ to be the quotient set $\pi_0(X, x_0) / i_*\bigl(\pi_0(A, x_0)\bigr)$ so that the long exact sequence of homotopy groups for the pair $(X, A)$ extends to $\cdots \to \pi_0(A, x_0) \stackrel{\iota_*}{\longrightarrow} \pi_0(X, x_0) \to \pi_0(X, A, x_0) \to 0$.

(a) Show that with this extension, the five-lemma holds for the map of long exact sequences induced by a map $(X, A, x_0) \to (Y, B, y_0)$, in the following form: One of the maps between the two sequences is a bijection if the four surrounding maps are bijections for all choices of $x_0$.

(b) Show that the long exact sequence of a triple $(X, A, B, x_0)$ can be extended only to the term $\pi_0(A, B, x_0)$ in general, and that the five-lemma holds for this extension.
:::

::: {.solution}
Define, for a pointed pair $(X,A,x_0)$,
$$
\pi_0(X,A,x_0)=\pi_0(X,x_0)\big/\,i_*\pi_0(A,x_0),
$$
the quotient pointed set, so that every component of $X$ meeting $A$ becomes the distinguished element. Then
$$
\pi_0(A,x_0)\xrightarrow{i_*}\pi_0(X,x_0)\xrightarrow{j_*}\pi_0(X,A,x_0)\longrightarrow0
$$
is exact as a sequence of pointed sets: the components mapping to the distinguished relative class are exactly those meeting $A$, and $j_*$ is onto. Exactness of the whole extended sequence at every other term is Theorem 4.3 (p. 344).

Throughout, a map of pairs $\varphi:(X,A,x_0)\to(Y,B,y_0)$ induces a ladder between the two sequences, commutative by naturality of the long exact sequence (p. 345), and "exact" for pointed sets means that the image of one map is the fiber of the next over the distinguished element.

### (a) The five-lemma

*Terms of degree $\ge2$: the group case.* The standard five-lemma argument applies verbatim in a window of five group terms, since every map there is a homomorphism. Write the ladder as
$$
A\xrightarrow{f}B\xrightarrow{g}C\xrightarrow{h}D\xrightarrow{k}E
\quad\text{over}\quad
A'\xrightarrow{f'}B'\xrightarrow{g'}C'\xrightarrow{h'}D'\xrightarrow{k'}E'
$$
with all four squares commutative and both rows exact.

- *Injectivity of $\gamma:C\to C'$*, given $\alpha$ onto and $\beta,\delta$ one-to-one: if $\gamma(c)=1$ then $\delta h(c)=h'\gamma(c)=1$, so $h(c)=1$ and $c=g(b)$ for some $b$. Then $g'\beta(b)=\gamma g(b)=1$, so $\beta(b)=f'(a')$ for some $a'$, and $a'=\alpha(a)$ because $\alpha$ is onto. Hence $\beta(b)=\beta f(a)$, so $b=f(a)$ by injectivity of $\beta$, and $c=g(b)=gf(a)=1$.
- *Surjectivity of $\gamma$*, given $\beta$ and $\delta$ onto and $\varepsilon$ one-to-one: for $c'\in C'$ put $d'=h'(c')$ and choose $d\in D$ with $\delta(d)=d'$. Then $\varepsilon k(d)=k'\delta(d)=k'h'(c')=1$, so $k(d)=1$ because $\varepsilon$ is injective, and hence $d=h(c)$ for some $c\in C$. Now $h'(\gamma(c))=\delta h(c)=d'=h'(c')$, so $h'(\gamma(c)^{-1}c')=1$ and therefore $\gamma(c)^{-1}c'=g'(b')$ for some $b'\in B'$; choose $b\in B$ with $\beta(b)=b'$ and put $c''=c\,g(b)$. Then $\gamma(c'')=\gamma(c)g'(b')=c'$.

*Which windows these are.* The four terms of degree one or zero in the extended sequence are the pointed sets $\pi_1(X,A,x_0)$, $\pi_0(A,x_0)$, $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$, and they occur in the order

$$
\cdots\to\pi_{n+1}(X)\to\pi_{n+1}(X,A)\to\pi_n(A)\to\pi_n(X)\to\pi_n(X,A)\to\pi_{n-1}(A)\to\cdots,
$$

so a window of five consecutive terms all of which are groups is exactly one centered at a term of degree $\ge2$. The windows centered at $\pi_1(A,x_0)$, $\pi_1(X,x_0)$, $\pi_1(X,A,x_0)$ and in degree $0$ contain a pointed set, and the group chase says nothing about them. What is settled about the degree-zero window is stated below; about the two terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$ nothing below settles it, and the state of that question is recorded there.

*The question at those two terms is open, and disputed.* Whether the printed claim holds at the term $\pi_1(X,A,x_0)$ and at the term $\pi_0(A,x_0)$ is not settled on this card. Two counterexamples were proposed for it on 2026-11-14 and are withdrawn: the first is disputed on the ground that its vertical map $\pi_0(X)\to\pi_0(Y)$ is not then a bijection, and the second on the ground that $\pi_1(X,A,x_0)$ is to be read as having one class for each component of $A$ rather than one for each point of $A$, which makes the surrounding map at that term fail instead. The second objection is about the definition of $\pi_1$ of a pointed pair rather than about an example, so this question is being settled by a formal statement and not argued in prose: <https://github.com/dzackgarza/lean-categories/issues/156>. The claim of 2026-11-14 that the printed (a) fails at those two terms is withdrawn with the examples, and this card now asserts neither that it fails there nor that it holds there.

*The example this card gave before 2026-11-14 does not satisfy the hypothesis.* It took $X=\{x_0\}\sqcup\{a\}$ with $A=X$, $Y=\{y_0\}\sqcup[0,1]$ with $B=\{y_0,0,1\}$, $\varphi(x_0)=y_0$ and $\varphi(a)=0$. At the basepoint $x_0$ its four surrounding maps are bijections and $\pi_0(A,x_0)\to\pi_0(B,y_0)$ is not onto, but the hypothesis is that the four surrounding maps are bijections for all choices of basepoint, and at the basepoint $a\in A$ the vertical map at $\pi_1(X,A,a)$ fails to be a bijection: $X$ is discrete and the only path from $A$ to $a$ is the constant one, so $\pi_1(X,A,a)$ is one point, while $\pi_1(Y,B,\varphi(a))=\pi_1(Y,B,0)$ has two elements, the classes of the constant path at $0$ and of a path from $1$ to $0$, both of which start in $B$. That example is withdrawn, and nothing replaces it on this card: the question it was offered against is the open one recorded above.

*What does hold in degree zero.* The last three terms are pointed sets, where the group chase gives nothing. Three statements are available.

*Claim 1.* If the vertical maps at $\pi_0(A,x_0)$ and at $\pi_0(X,x_0)$ are bijections, then so is the vertical map at $\pi_0(X,A,x_0)$. Indeed that map is induced by a bijection $\pi_0(X,x_0)\to\pi_0(Y,y_0)$ which carries the subset $i_*\pi_0(A,x_0)$ bijectively onto $i_*\pi_0(B,y_0)$, and a bijection of sets carrying one subset onto another induces a bijection of the quotients.

*Claim 2.* If the vertical map at $\pi_1(X,A,x_0)$ is onto, then every component of $B$ that lies in the component of $y_0$ in $Y$ is the image of a component of $A$: such a component is $\partial'\xi$ for some $\xi\in\pi_1(Y,B,y_0)$, because exactness at $\pi_0(B,y_0)$ says the image of $\partial'$ is the fiber of $\pi_0(B,y_0)\to\pi_0(Y,y_0)$ over the distinguished element; lift $\xi$ to $\eta$, and then $\varphi(\partial\eta)=\partial'(\varphi_*\eta)=\partial'\xi$ by naturality of $\partial$.

*Claim 3.* If the vertical maps at $\pi_1(X,A,x)$ are onto for every $x\in A$, and those at $\pi_0(X,x_0)$ and $\pi_0(X,A,x_0)$ are bijections, then the vertical map at $\pi_0(A,x_0)$ is onto. For let $\beta$ be a component of $B$ and $C$ the component of $Y$ containing it. Since the map at $\pi_0(X,x_0)$ is onto, $C=\varphi(D)$ for a component $D$ of $X$. If $D$ meets $A$, take $a\in D\cap A$; the point $\varphi(a)$ lies in $C\cap B$, hence in a component $\beta'$ of $B$ inside $C$, and Claim 2 applied at the basepoint $a$ gives that $\beta$ is the image of a component of $A$, which is what was to be shown if $\beta'\ne\beta$, while $\beta'=\beta$ is the same conclusion directly. If $D$ does not meet $A$, then $D$ is not in $i_*\pi_0(A,x_0)$, so the class of $D$ in $\pi_0(X,A,x_0)$ is not the distinguished element, and injectivity of the map at $\pi_0(X,A,x_0)$ makes the class of $C=\varphi(D)$ in $\pi_0(Y,B,y_0)$ non-distinguished, that is, $C$ meets no point of $B$ — but $\beta\subset B\cap C$. So the second case cannot occur.

Thus the hypothesis forces surjectivity at $\pi_0(A,x_0)$, whatever else it forces there: if the printed claim fails at that term it fails by injectivity, and the example of 2026-11-07 was offered against surjectivity and so could not have been evidence for that.

*Not settled on this card.* The windows centered at $\pi_1(A,x_0)$ and at $\pi_1(X,x_0)$ have the pointed set $\pi_1(X,A,x_0)$ among their surrounding terms, so the group chase does not reach them, and this card neither proves them nor gives an example against them. Injectivity of the vertical map at $\pi_1(X,x_0)$ does follow from injectivity at $\pi_1(X,A,x_0)$, since a loop at $x_0$ is a path from $A$ to $x_0$ and the classes agree; surjectivity does not follow by that argument, because a path from $A$ to $x_0$ whose image is a given loop need not itself be a loop.

### (b) The triple sequence

For $B\subset A\subset X$ the triple sequence of Theorem 4.3 ends
$$
\cdots\longrightarrow\pi_1(X,A,x_0)\xrightarrow{\partial}\pi_0(A,B,x_0),
$$
and it cannot in general be continued by $\pi_0(X,B,x_0)$. Take $X$ the disjoint union of a point $b_0$ and an interval, $x_0=b_0$, and $B=\{b_0,b_1\}$ with $b_1$ a point of the interval; let $A=\{b_0,b_1,a_1\}$ with $a_1\neq b_1$ a further point of the interval, so that $b_1$ and $a_1$ lie in different components of the subspace $A$ while lying in the same component of $X$. Then the class of $a_1$ in $\pi_0(A,B,x_0)=\pi_0(A,x_0)/i_*\pi_0(B,x_0)$ is not the distinguished element, because its component of $A$ does not meet $B$; but its image in $\pi_0(X,B,x_0)$ is distinguished, because every component of $X$ that meets $B$ is collapsed and $a_1$ lies in the component of $b_1$. On the other hand the class of $a_1$ is not in the image of $\partial:\pi_1(X,A,x_0)\to\pi_0(A,B,x_0)$, since a path in $X$ starting in $A$ and ending at $x_0=b_0$ stays in the component $\{b_0\}$ of $X$, so its starting point lies in the component $\{b_0\}$ of $A$, which is collapsed. Hence appending $\pi_0(X,B,x_0)$ would destroy exactness at $\pi_0(A,B,x_0)$.

With the sequence ending at $\pi_0(A,B,x_0)$, the five-lemma holds for the ladder of triple sequences up to that terminal term, with the same qualifications as in (a): the windows of group terms are covered by the group case, and the terminal term is a quotient of pointed sets, where the analogue of Claim 2 applies with $B$ in the role of the subgroup and $A$ in the role of the pair.
:::

::: {.remark title="Sources"}

The exercise is Exercise 9 of §4.1, printed p. 358, stated with the errata's $i_*$ in place of $i^*$. What this card proves is the group chase at every term of degree $\ge2$ and Claims 1, 2 and 3 in degree zero; what it records as open is whether the printed claim holds at the terms $\pi_1(X,A,x_0)$ and $\pi_0(A,x_0)$, which is settled by a formal statement rather than in prose, <https://github.com/dzackgarza/lean-categories/issues/156>, together with the windows named in the last paragraph of (a). No published treatment of this exercise was located, in the retained sets or in the sources searched for it.

A related published statement, cited for exactly what it proves: **R. Brown, *Fibrations of groupoids*, Journal of Algebra 15 (1970), 103--132**, Theorem 4.9 on printed p. 121 and Corollary 4.11 on printed pp. 122--123 (reading copy `tmp/sources/brown-1970-fibrations-of-groupoids.md`). For a fibration of groupoids $p:G\to H$ with fibre $F$ over an object $v$, Brown's 4.9(a) concludes that $f:\pi_0F\to\pi_0F'$ is surjective if the maps of vertex groups $h:H(v)\to H'(v')$ and of components $g:\pi_0G\to\pi_0G'$ are surjective and $h:\pi_0H\to\pi_0H'$ is injective, and 4.9(b) concludes that $f$ is injective on $\ker(i:\pi_0F\to\pi_0G)$ if $h:H(v)\to H'(v')$ is injective and $g:G(x)\to G'(x')$ is surjective; Corollary 4.11 concludes that $h:H\to H'$ and $g:G\to G'$ being equivalences of groupoids forces $f:F\to F'$ to be an equivalence, in particular $f:\pi_0F\to\pi_0F'$ to be a bijection, the proof applying 4.9 and then the ordinary five-lemma for groups to Brown's diagram 4.8. That is a five-lemma at the $\pi_0$ term, and its hypotheses are stronger than the exercise's: an equivalence of groupoids is a bijection on hom-sets at every object and on components, which is the exercise's "for all choices of $x_0$" in a setting where a fibration supplies the exact sequence. It is a statement about fibrations of groupoids, and the map of pairs $(X,A)\to(Y,B)$ is not one, so nothing above rests on it, and it neither asserts nor denies the failures this card records.

:::
