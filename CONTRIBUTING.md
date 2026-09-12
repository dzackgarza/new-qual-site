# Contributing

Contributions can improve mathematical content, source records, study guides, or the website.

## Named policies

Use these stable identifiers in contributions and review. [AGENTS.md](AGENTS.md)
retains the detailed authoring rules; [REVIEW_POLICY.md](REVIEW_POLICY.md) retains
the existing named advisory defect patterns.

| ID | Name | Required action |
| --- | --- | --- |
| `QUAL-01` | Source-faithful mathematics | Read the complete card and relevant source before changing a statement, title, classification, relation, or proof. Preserve hypotheses and every requested part. |
| `QUAL-02` | Semantic authorship | Decide mathematical meaning by reading. Measurements and matching names identify candidates; they do not decide equivalence, correctness, or deletion. |
| `QUAL-03` | One card, one proof owner | Author and review one card at a time. Solutions and hints belong in their problem card; commit the reviewed card before continuing. |
| `QUAL-04` | Dependency-directed work | Use [the TODO DAG](TODO.md#execution-dag). Give each concrete task a stable ID, immediate prerequisites and an observable result. Preserve the scope of unfinished work and reject cycles or unresolved prerequisite IDs. |
| `QUAL-05` | Capture issues when encountered | Record mathematical errors, source ambiguities, and actual papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries. Supply evidence, affected card or owner, expected result, uncertainty, and a repair link. Extend an existing entry for the same issue. Logging is not repair. |
| `QUAL-06` | Match verification to the artifact | Read mathematical proofs for correctness; a parser cannot certify them. For renderer or styling changes, render and inspect the actual affected pages. Use existing just recipes and the prose-only commit exemption where applicable. |
| `QUAL-07` | Preserve concurrent authorship | Reread target files before editing, preserve others' changes and staged files, and commit only the intended paths. Keep complaint and TODO edits confined to the selected entry. |
| `QUAL-08` | Keep process off public cards | Store issue capture here and in COMPLAINTS/TODO, not in rendered remarks. Mathematical errata may explain a false statement and its corrected hypotheses on the card. |
| `QUAL-09` | One checkout, one branch | Work directly on `main` in the single clone. Do not create worktrees or branches: streams author disjoint cards, so there is nothing to isolate. A commit that sweeps in a sibling's edit is a wrong message, not lost work — `git commit --amend`, or commit an explicit pathspec. Before retiring a worktree left over from the old rule, take all three readings — clean tree, commits reachable from `main`, no live process — and leave it in place and report it if any one fails. |

## Requirements

- Python 3.14

- [uv](https://docs.astral.sh/uv/)

- [just](https://just.systems/)

- [Pandoc](https://pandoc.org/) with the `pandoc server` command

## Setup

```sh
git clone https://github.com/dzackgarza/new-qual-site.git
cd new-qual-site
uv sync --group dev
```

## Working in the clone

Every stream works directly on `main` in this one checkout, using the environment
`uv sync --group dev` created above. Do not create worktrees and do not create
branches: streams author disjoint cards, so there is nothing for a branch to
isolate. If a commit sweeps in a sibling's concurrent edit, that is a wrong commit
message rather than lost work — `git commit --amend`, or commit the paths you meant
with an explicit pathspec as `QUAL-07` already requires.

Worktrees left over from the previous rule are retired under `QUAL-09`; see
[AGENTS.md](AGENTS.md#one-checkout-one-branch) for what each reading establishes.

## Repository structure

- `corpus/` contains problems, sources, definitions, theorems, proofs, hints, and solutions.

- `publications/` orders cards into subject guides and reading paths.

- `vocabularies/` contains shared topics, institutions, textbooks, citations, and MathJax macros.

- `tools/qualc/` contains the corpus compiler and static-site generator.

- `site/` contains browser code and styles.

- `build/` contains generated files. Do not edit them.

## Mathematical content

Read the relevant cards before changing their titles, classifications, relations, or content.
Make semantic decisions from the mathematics, not from filenames or text similarity.
In card titles, use ordinary mathematical notation instead of spelling simple
formulas out in words (`$L^2$`, `$\ZZ^3/N$`, `$x^8-1$`, not “L2”, “Z cubed
mod N”, or “x to the eighth minus one”). Keep conceptual prose as prose.

Public prose must state mathematical content. Do not address an imagined student
or exam prompt, announce that a theorem or question “matters”, or point to “the
next question” without naming the mathematical relation. Replace those phrases
with the definition, hypothesis, result, consequence, or technique they were
standing in for. See the [prose policies](#prose-policies) for bad and good
replacements.

A canonical problem states one mathematical problem.
An exam or textbook collection lists those problems in the order they appeared.
Appearances on a problem page are generated from that list.

Use an existing card of the same kind as the format example.
The compiler rejects unknown fields, unknown card kinds, invalid relations, and unregistered vocabulary.

## Build the site

Check the corpus:

```sh
just check
```

Build the catalog and website:

```sh
just build
```

Preview the website:

```sh
just preview
```

Open <http://localhost:8000> after the preview server starts.

Run `just --list` for the current development commands.

## Prose policies

These policies apply to all public card, guide, and wiki prose. They identify
patterns that spend the reader's attention on an imagined teaching situation
instead of supplying mathematical content. Such prose also depends on page
order, assignment context, or an unstated reader mistake. A textbook reader
needs statements that can be read, cited, and used without reconstructing that
hidden situation.

### `PROSE-01`: State the mathematical payload instead of its importance

**Bad:** “The question that matters is whether the construction is local.”

**Good:** “A scheme is a locally ringed space that is locally isomorphic to
`Spec(A)` for a commutative ring `A`. The definition is local on affine
neighborhoods.”

“Matters”, “important”, “useful”, and “central” do not identify a result,
hypothesis, consequence, or technique. Delete the judgement or replace it with
the fact that gives it value.

### `PROSE-02`: Address the mathematics, not an imagined assignment

**Bad:** “You are asked to define a scheme.”

**Good:** “A scheme is a locally ringed space whose points have affine
neighborhoods.”

An assignment prompt belongs in a problem statement when the assignment itself
is the mathematical object. In exposition, the reader needs the definition or
the result. The prompt supplies no mathematical claim and forces the reader to
adopt an invented exam frame.

### `PROSE-03`: Name the relation instead of pointing by position

**Bad:** “The question that matters is the next one.”

**Good:** “After defining the affine charts, check whether the transition maps
are compatible on overlaps.”

“Next”, “above”, and “below” are properties of document layout. They are not
mathematical referents. Page order changes when text is split, transcluded, or
rendered in another context. Name the object, map, hypothesis, or claim that
the reader must use; if no such relation exists, remove the signpost.

### `PROSE-04`: Do the mathematics instead of describing the document

**Bad:** “This page gives the framework for understanding schemes.”

**Good:** “A scheme is a locally ringed space that is locally isomorphic to
`Spec(A)` for a commutative ring `A`.”

Self narration describes the page instead of supplying its subject. A reader
can see the page and needs the definition, result, or example that the sentence
claims to introduce.

### `PROSE-05`: Remove negative framing that rejects no real alternative

**Bad:** “A scheme is not merely a topological space with extra information.”

**Good:** “A scheme consists of a topological space and a sheaf of rings whose
stalks are local rings.”

“Not merely”, “rather than”, and “never” often invent a mistaken view for the
reader to reject. State the positive structure. Keep a contrast only when the
contrast is a mathematical counterexample or distinction with a named object.

### `PROSE-06`: Do not certify the text inside the text

**Bad:** “The definitions below are complete and arranged in dependency order.”

**Good:** Put the definitions in the required order and let the links and
headings show that order.

A sentence cannot make the page complete, canonical, minimal, or self contained.
Those properties belong to the artifact and its checks. The sentence spends
space asserting a property that the reader must verify from the page.

### `PROSE-07`: Do not tell the reader how to read

**Bad:** “Keep this distinction in mind when reading the proof.”

**Good:** “The morphism is an isomorphism only when it is bijective on the
underlying spaces and induces isomorphisms on all stalks.”

Theory of mind replaces a mathematical claim with instructions about attention,
memory, or interpretation. State the distinction where the reader uses it.

### `PROSE-08`: Remove puffery and cadence padding

**Bad:** “This powerful and elegant theorem is a crucial bridge between the two
deep theories. Moreover, it is worth noting that it is broadly useful.”

**Good:** “If $X$ is projective over a field, every regular function
$X\to\mathbb A^1$ is constant.”

Adjectives such as “powerful”, “deep”, “crucial”, and “elegant” rate the subject
without stating it. Formulaic transitions and lists of three create rhythm
without adding evidence. Delete them or replace them with the result or its
application.

### `PROSE-09`: State the theorem before its notational consequence

**Bad:** “Coherence is what lets us write a tensor product without
parentheses.”

**Good:** “The coherence theorem identifies all composites of associators with
the unique canonical isomorphism between any two parenthesizations. We therefore
write the tensor product without parentheses.”

The notation is justified by a precise theorem. Naming only the notational
payoff hides the object, map, and equality that the theorem controls.

### `PROSE-10`: Separate construction from verification

**Bad:** “Take the product as the tensor operation and use the unique maps from
the universal property, which gives a monoidal category.”

**Good:** “Define $A\otimes B=A\times B$ and take the terminal object as the
unit. The universal properties of products supply the associator and unitors;
their coherence follows from uniqueness.”

A construction answers what is chosen. A verification answers why it has the
required properties. Combining both in one sentence hides that logical order.

### `PROSE-11`: Keep project process out of mathematical exposition

**Bad:** “This theorem is included because the audit requires it.”

**Good:** State the theorem and its hypotheses. Record audit or authoring
information in this guide or in the repository work queues.

Readers need mathematical reasons for mathematical claims. Internal workflow,
review status, and implementation reasons belong in contributor documentation.

## Precision policies

These policies prevent prose from taking the place of a typed mathematical
statement. The general reason is the same in each case: a reader must be able
to identify the objects, maps, hypotheses, and conclusion without guessing.

### `PRECISION-01`: Replace mood words with definitions

**Bad:** “A scheme is a geometrically complete space.”

**Good:** “A scheme is a locally ringed space locally isomorphic to the spectrum
of a commutative ring.”

Vibe adjectives sound technical while leaving the defining conditions unknown.
Use the standard term and state its definition.

### `PRECISION-02`: Replace vague qualifiers with exact scope

**Bad:** “This holds essentially for finite type schemes.”

**Good:** “This holds for schemes locally of finite type over a field.”

Words such as “essentially”, “basically”, “morally”, and “in some sense” hide
the hypothesis or weaken a claim without saying how. State the exact scope, or
name a genuine approximation such as “up to isomorphism”.

### `PRECISION-03`: Name operations instead of using empty collective nouns

**Bad:** “The construction carries the required structure.”

**Good:** “The pullback sheaf has restriction maps satisfying the sheaf axiom.”

“Data”, “structure”, “property”, “framework”, “package”, and “setting” are
acceptable only when they have a fixed mathematical referent. Otherwise they
hide the operations or axioms the reader must check.

### `PRECISION-04`: State universal constructions as universal constructions

**Bad:** “Define $E\to X$ by pulling back $U\to B$ along $X\to B$.”

**Good:** “Let $E$ be the pullback in the Cartesian square
$E\to U$, $E\to X$, $U\to B$, $X\to B$.”

“Obtained by pulling back” is an instruction without the square, maps, or
universal property. Give the diagram or state the property that characterizes
the object.

### `PRECISION-05`: Bind symbols before using them

**Bad:** “The map $f$ is surjective, where $X$ is the source.”

**Good:** “For schemes $X$ and $Y$, let $f\colon X\to Y$ be a morphism. Assume
$f$ is surjective.”

An unbound symbol forces the reader to recover its type and scope from later
prose. Introduce every object, map, index, and codomain before its first use.

### `PRECISION-06`: Give every map its domain and codomain

**Bad:** “Consider the natural map $f$.”

**Good:** “Consider the natural morphism $f\colon X\to Y$ induced by the ring
map $A\to B$.”

A map without its source, target, and construction cannot be checked or composed.
The type is part of the mathematical statement.

### `PRECISION-07`: Use standard terms and notation

**Bad:** “The value space of $M$” when the object is an $R$-module $W$.

**Good:** “Let $b\colon M\otimes_R M\to W$ be a $W$-valued bilinear form.”

Invented terms and elegant variations make readers guess whether a new object
was introduced. Use the standard name, or define the new term before using it.

## Structure policies

These policies protect the logical skeleton of the book. A section or example
must carry a mathematical unit that a reader can identify and reuse.

### `STRUCTURE-01`: Give each definition one defining occurrence

**Bad:** Define “scheme” in a lede, restate it in a remark, and use both
versions as if they had equal authority.

**Good:** Give one fenced definition, then link to it and state consequences
where they are used.

Multiple defining occurrences drift apart and make it unclear which hypotheses
govern later claims. One defining occurrence gives the term a stable referent.

### `STRUCTURE-02`: Put a primary mathematical unit in every section

**Bad:** A section contains only “This is useful for the next chapter” and a
list of links.

**Good:** Give the section a definition, theorem, example, counterexample, or
worked calculation, then use remarks and links to support it.

Without a primary unit, a section is navigation or process prose disguised as
exposition. Secondary remarks cannot carry the chapter's logical skeleton.

### `STRUCTURE-03`: Keep examples subordinate to the definition they illustrate

**Bad:** “Affine space is an important example of a scheme.”

**Good:** “For a ring $A$, the locally ringed space $\operatorname{Spec}(A)$ is
an affine scheme. When $A=k[x_1,\ldots,x_n]$, it is affine $n$-space over
$k$.”

An example should instantiate the defining data. Calling something an example
without showing the instance gives the reader no mathematical test.

### `STRUCTURE-04`: State propositions as propositions

**Bad:** “The following is the key fact about proper morphisms.”

**Good:** “A proper morphism of schemes is universally closed, separated, and
of finite type.”

Labels such as “key fact” and “important result” announce status instead of
stating a claim. Name the hypotheses and conclusion so the reader can apply it.

### `STRUCTURE-05`: Use references for mathematical referents

**Bad:** “As discussed above, this map is an isomorphism.”

**Good:** “By the normalization theorem, the induced map is an
isomorphism.”

Position and memory are unstable references. Link the named theorem, card, or
page when the reader must use it.

### `STRUCTURE-06`: Use parentheticals only for genuine qualifications

**Bad:** “The map is finite (and this is important, as we will see below).”

**Good:** “The map is finite (equivalently, the target coordinate ring is a
finite module over the source coordinate ring).”

Parentheticals should restrict or identify the claim. If they only announce
future explanation, motivation, or emphasis, move the mathematical content into
the main sentence or delete the parenthetical.
