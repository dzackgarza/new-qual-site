# Mathematical issues and papercuts

Record issues encountered during source reading, solving, review, authoring or
site use under [QUAL-05](CONTRIBUTING.md#named-policies). Include findings outside
the selected card. This file owns observations; [TODO.md](TODO.md) owns selected
repair tasks and dependencies. Keep existing GitHub issue links rather than
copying their live status. The [review policy index](REVIEW_POLICY.md) supplies
named candidate patterns, not proof that a candidate is a defect.

## Recording an issue

Add a descriptive heading in the appropriate section below, with:

- **Object and need:** card/collection ID or affected workflow; the exact
  mathematical statement and hypotheses, or user action and expected behavior.
- **Observed evidence:** source page and passage, counterexample or proof gap,
  or actual action and result with the relevant path/revision.
- **Impact and owner:** affected parts or consumers, existing partial result,
  and the mathematical or tool boundary that must change.
- **Uncertainty:** distinguish a verified error from a source ambiguity or
  review candidate. State inspected scope and remaining questions. For absence
  claims supply Searched, Found, Conclusion, Confidence and Gaps.
- **Repair:** link the existing TODO task or issue when available and state
  the result that would resolve the observation.

A missing hypothesis with a concrete counterexample is a mathematical issue.
An unreadable source is an unresolved source question. An unsolved problem is
ordinary authoring work, not by itself a defect. A command that prevents reading
the intended card is a papercut even when it has a simple workaround.

Extend an existing entry when the same cause affects another card. Preserve
concurrent entries. If the selected proof requires a repair, link that dependency
and resolve it before relying on the statement; recording it does not make the
proof valid. Continue independent assigned mathematics.

After verifying the full repair, remove the resolved entry with evidence in the
fixing commit; retain any unresolved portion. Put durable mathematical errata
on the owning card and durable policy in CONTRIBUTING. Keep process notes out
of public mathematical remarks.

## Mathematical issues and source questions

### The 2003–2009 algebra packet has mixed subject metadata

- **Summer 2014 source-checked repairs:** problems 1, 3, 4, and 6 in the retained 2010–2015 packet confirm `P-TNZTM`, `P-WC2SP`, `P-JHQKZ`, and `P-ZR3OT` as algebra, although each card had sole area `prelim`. Commits `22cb7e0f9`, `a4a9b4527`, `fd3e6433d`, and `2d22e4b57` correct those classifications and supply all requested proofs or counterexamples. The tensor-product card also moves the source's inline hint to a separate hint section and retains the noncommutative-ring hypothesis throughout the proof. These are dispositions of the inspected cards, not of other cards sharing the label.

- **July 2013 source-checked repairs:** visual inspection of PDF pages 6–8 confirms `P-XVV4O`, `P-IXED6`, `P-RP7WR`, and `P-ZG74L` as algebra, although each had sole area `prelim`. Commits `0150fd7f8`, `2a286da3a`, `3ec7685f5`, and `63d2c16c7` correct those classifications and supply complete solutions. The congruence card formerly referred to an unspecified earlier problem for the definition of ideal join; `2a286da3a` incorporates the definition from Rings 1 on the same source page, preserving the hypotheses and making the statement self-contained.

- **Same defect in the later packet:** June 2015 Groups 3, Rings 2, and Fields 2–3 in `algebra_2010-2015_prelims.md` verify `P-PCSZ2`, `P-HHX6V`, `P-U64DA`, and `P-VFB5V` as algebra, although each had sole area `prelim`. Commits `565de6d8f`, `761157381`, `ac07d741f`, and `dc8660316` repair those four classifications individually with complete proofs. The first also makes the source's identity-bijection qualification explicit in the title; the second replaces an unrelated Free Modules topic with Principal Ideal Domains. These four confirmed cases are resolved; they do not establish a disposition of unread classification candidates.

- **Additional source-checked repair:** page 5, Rings and modules 3, confirms `P-TB7BG` as algebra. Commit `8ed9d41e6` corrects that classification and replaces its invalid nilpotency argument with a complete invariant-complement proof. The two explicit algebraic counterexamples remain in the card's mathematical remark; its proof defect is resolved. Other classification candidates in this entry remain subject to individual source review.

- **Further verified repairs:** Summer 2007 Rings 1 and 3 confirm the algebra classifications of `P-PDAPQ` and `P-ZSFKA`, corrected in `fdfd7e73b` and `019c900b6`. The latter also resolves the signed-norm ambiguity by stating the absolute norm and proving Euclidean division, with the source convention explained on the card.

- **Object and need:** `SRC-ART-ALG-2003-2009-PRELIMS`; cards should be filed by the mathematical subject of the source rather than by the generic word “prelim.”
- **Observed evidence:** the original Summer 2009 Algebra Qualifying Exam, page 2, Rings 3–4, confirms algebra content for `P-CSEAZ` and `P-JH3BD`, but both cards had sole area `prelim`. Their source-backed solution edits correct those two areas. A subsequent `rg -l '^  - prelim$' corpus/collections/SRC-ART-ALG-2003-2009-PRELIMS` returned 11 other cards, including `P-3DS32`, `P-GW4KD`, `P-PDAPQ`, and `P-ZSFKA`.
- **Impact and owner:** subject-based browsing can file algebra questions under prelim. This collection owns source-backed classification repairs.
- **Uncertainty:** the original literal search was restricted to this collection and returned 11 review candidates. `P-TB7BG`, `P-PDAPQ`, and `P-ZSFKA` have since been individually source-checked and repaired; the other candidates are not individually verified defects in this entry.
- **Repair:** read each remaining candidate with its source and correct confirmed subject mismatches, preserving any genuinely intended prelim classification rather than applying a bulk substitution.

### P-4IKKY is internally inconsistent as transcribed

- **Object and need:** `P-4IKKY` in `SRC-UGA-ALG-FALL-2012`; the card should state a nonvacuous structure theorem for an infinite-dimensional vector space equipped with a linear operator.
- **Observed evidence:** the card assumes that the infinite-dimensional $k$-vector space $U$ is generated by the finite set $\{u_1,\ldots,u_m,f^d(u_1),\ldots,f^d(u_m)\}$ for one fixed $d\in\NN$. Such a span has dimension at most $2m$, contradicting the hypothesis that $U$ is infinite-dimensional. The preserved Fall 2012 transcription on the project site reproduces the same wording.
- **Impact and owner:** the literal hypotheses have no models, so attaching the intended $k[x]$-module structure-theorem proof would require guessing missing quantifiers and invariance hypotheses. In particular, the likely intended family $\{f^d(u_i):d\ge0\}$ is not what the source currently states.
- **Uncertainty:** the mathematical inconsistency is decisive, but no independent copy of the Fall 2012 source has yet been recovered that supplies the missing quantification or clarifies the uniqueness clause.
- **Repair:** recover an independent source or erratum for Fall 2012 problem 5 and restore the quantification on the iterates, together with whatever $f$-invariance/module hypotheses are required, before attaching the intended proof.

### P-MMAQ-WV7QEYSPXM omits the infinite-cyclic injectivity hypothesis

- **Object and need:** `P-MMAQ-WV7QEYSPXM`, Dummit--Foote §5.5 Exercise 6; the local statement must retain every hypothesis needed for the semidirect-product isomorphism.
- **Observed evidence:** the local card states the result for an arbitrary cyclic group $K$. Dummit--Foote's exercise adds: if $K$ is infinite, assume both $\varphi_1$ and $\varphi_2$ are injective. The same wording is independently reproduced in University of Utah Math 6320 Exercise 4 (DF-5.5.6-7).
- **Impact and owner:** without injectivity in the infinite case, conjugate finite cyclic images can be generated by different powers while the corresponding power map $K\to K$ is not an automorphism, so the requested construction is not justified. The problem card owns the repair.
- **Uncertainty:** the omitted clause is verified against two reproductions of the source exercise; no ambiguity remains about the intended hypothesis.
- **Repair:** restore the infinite-case injectivity clause on `P-MMAQ-WV7QEYSPXM` before attaching a proof.

### P-HGRO11 does not specify the coefficient field

- **Object and need:** `P-HGRO11` in `SRC-HARVARD-GROUPS-ORAL`; deciding whether a determinant-one matrix group is simple requires the coefficient field and whether the intended group is $SL_2(F)$ or its projective quotient.
- **Observed evidence:** both the preserved Harvard source extraction and the local card ask only whether “the group of $2\times2$ matrices of determinant $1$” is simple, with no coefficient field. For example, if $\operatorname{char}F\ne2$, then $-I$ is a nontrivial central element of $SL_2(F)$, while simplicity statements for $PSL_2(F)$ depend on $F$.
- **Impact and owner:** there is no source-faithful yes/no answer to the card as written. The Harvard group-orals source/card record owns recovery of the intended field or clarification that the question concerns a particular projective special linear group.
- **Uncertainty:** verified against the retained Harvard PDF extraction; the omitted field may have been supplied orally or by surrounding course context not present in the preserved question list.
- **Repair:** recover the intended coefficient field/group from an independent Harvard source or explicitly mark the source question as underdetermined before solution authorship resumes.

## Workflow and rendering papercuts

### The configured PDF extraction command is missing and service requests failed

- **July 2013 symbol recovery:** the retained extraction drops the divisibility symbol in Groups 1(b). Visual inspection of PDF page 6 confirms `p` does not divide `q-1`, exactly as stated on `P-W13PQ`. The web reader returned an internal error for the public raw PDF and a non-retryable rejection for the CDN URL, so neither yielded a PDF that its screenshot tool could inspect. Rendering the retained PDF with the installed system PDFium and inspecting the resulting page image succeeded without OCR or a new text extraction. The card's hypothesis needed no correction.

- **July 2003 lattice recovery:** `P-ARTALG-JU03-6` replaced its essential diagram with the undefined phrase “a specific diamond shape.” Native inspection of PDF page 45 shows exactly four incomparable middle vertices, plus top and bottom. Commit `6b1b83169` restores that complete order relation and proves all five decisions, including realization over the specified base field. For this inspection, `UV_NO_SYNC=1 uv run python` lacked `pypdfium2`; `/usr/bin/python3` already had it and rendered the retained source successfully without installing packages or running OCR. PDF page 44 contains problem 5, not the required diagram.

- **Object and need:** source verification for `P-ARTALG-AL04-3` exposed an unavailable configured PDF extraction command and subsequent remote-service failures. The installed source-reading workflow should be usable without guessing numeric hypotheses from extracted text.
- **Observed evidence:** on 2026-09-10, `command -v mineru-open-api` returned no executable, and `UV_NO_SYNC=1 uv run mineru-open-api --help` failed with `No such file or directory`. `AGENTS.md` names this command as the sole permitted PDF extraction method.
- **Execution attempts:** the official Linux binary runs from `/tmp/qual-mineru.XhPQVW/mineru-open-api` and reports version `v0.5.9`. A page-29-only `flash-extract` request timed out uploading the PDF. Separate URL-input requests using the public GitHub copy and a jsDelivr copy both returned error `-60007`, reporting that the model service was temporarily unavailable. Both public copies were verified byte-identical to the repository PDF before submission. All three requests targeted page 29; none returned source content.
- **Source verification, 2026-09-10:** direct PDFium rasterization of the retained PDF and native image inspection succeeded. Page 29 contains only Groups 1; the actual Groups 3 statement is on PDF page 30 (printed page 2) and says the integer `72`, with no superscript and no abelian hypothesis. The PDF SHA-256 is `956dd5e3735e66d75eb0bed9af4f0c544015016fcf48fec8f10eeab98a06393b`. No new text extraction or OCR was used. Commit `83522c224` retains order 72 and proves the full fifty-class classification, including the executable exact action-orbit enumeration.
- **Additional tool friction:** web retrieval of the public raw PDF returned `DisabledError`, alternative PDF URLs were rejected, and a combined read-only repository request was rejected before execution. Native reads and local rendering restored source access. The installed PDFium wrapper also rejected the context-manager form with `TypeError`; constructing `PdfDocument` directly succeeded. A later combined request for `P-ARTALG-JU03-9` single-card parsing and diff review was also rejected before execution; the two separated operations succeeded, so the rejection was not a failed repository check.
- **Additional source defect repaired:** visual inspection of PDF page 32 (printed page 4), Rings 2, showed that `P-ARTALG-AL04-6` omitted part (a), the rational canonical form of the matrix with rows `(2,3)` and `(7,1)`. Commit `7db3ccc00` restores and proves both parts on that source item; the garbled matrix in the extraction was not evidence that the original paper omitted it.
- **Additional proof defect repaired:** the former `P-ARTALG-AL04-10` proof inferred that a group is abelian from a normal abelian subgroup and a cyclic quotient; that implication is false, as `S3` with its normal `C3` shows. The order-specific action argument needed there was absent. Commit `d79880a9b` replaces it with the index-three coset action. PDF page 37 also prints `[K:F]=105` with `F` undefined; the already-authored card explicitly states `[K:Q]=105`, and that is the hypothesis proved rather than an assertion about an unspecified field `F`.
- **Additional collection omission repaired:** PDF page 38 (printed page 10) contains 2004 Fields 4, asking for all subfield orders of a field of order `5^20` and uniqueness of its subfield of order 25. The 2004 section listed only ten items, ending with Fields 3 on `P-ARTALG-AL04-10`; its four Groups, three Rings, and three Fields cards omitted this final source problem. A corpus-wide literal search for `5^{20}`, `5^20`, and `more than one subfield of order` returned no matches. Commit `420c00019` restores the item as `P-ARTALG-AL04-11`, its ordered membership, and the complete existence-and-uniqueness proof. Zero unsolved listed cards had not established complete source coverage.
- **Impact and owner:** the source ambiguity is resolved and no longer blocks this card. The missing configured command and remote-service failures remain setup/tooling issues; successful local rendering does not establish that those services were repaired.
- **Uncertainty:** the printed numeric hypothesis is now visually verified. The generic API errors do not establish a bad PDF, a credential failure, or a specific service-side cause.
- **Repair:** restore and document the configured extraction command and service. Source inspection of this card is complete; future page-specific requests must use the verified PDF page rather than the section's starting page.

### Single-card validation accepts duplicate YAML mapping keys

- **July 2013 reproduction:** `just check-card` reported schema and Markdown parsing OK for `P-W13IN` while the immediately following diff contained two top-level `audit` keys and two complete coset-action proofs. Both versions were read and found mathematically correct. A subsequent external edit removed the duplicate; `f2c54e941` contains the retained single proof and audit list. This resolves the card collision, not the parser's missing duplicate-key diagnostic.

- **Object and need:** `qualc.authoring check` must reject ambiguous duplicate mapping keys in card front matter, rather than reporting that the card parses correctly.
- **Observed evidence:** on 2026-09-10, `just check-card P-T4WCS` reported schema and Markdown parsing OK while the card had two top-level `audit` keys and two independently authored solution sections. Commit `cc3b2e722` preserves that exact duplicate-key example.
- **Impact and owner:** a syntactically accepted card can contain conflicting audit histories without a diagnostic. This entry concerns the card parser; the separate same-range ownership collision is recorded below.
- **Uncertainty:** this establishes a missed duplicate-key diagnostic in the single-card command, not the behavior of every loader or the full build. Multiple deliberately authored solutions are not themselves an error.
- **Repair:** reject duplicate mapping keys in card front matter. The particular card was reconciled in `f5f68b2db` after reading both correct proofs; the shorter support-and-transitivity argument was retained, with both original versions preserved in history. That content repair does not repair the parser.

### Supposedly disjoint collection streams collided on consecutive cards

- **July 2013 reproduction:** while this stream authored `P-W13IN`, a second writer independently appended the same coset-action proof and an additional top-level `audit` key. A fresh read later showed only this stream's visually source-checked proof; the other writer had removed its duplicate before the attempted commit. Both versions were independently reviewed. Later full-context source-check patches for `P-W5LVB` and `P-NGXAE` were rejected without changes after another writer had supplied complete proofs. Those proofs were read in full, checked against the source and the required exhaustive classifications, and preserved in commits `3d093c891` and `1d405a5b6`. Native `agents.status` again returned `WORKER_IDENTITY_LOST`, so the tool still supplied no addressable owner for coordination.

- **July 2003 reproduction, 2026-09-10:** `P-ARTALG-JU03-5` and `P-ARTALG-JU03-8` were each read without solutions and acquired another writer's complete solution before this stream's exact-context patch. Both patches were rejected without changes. The resulting proofs were read in full and preserved; this stream instead completed the still-unwritten lattice and solvability cards. The overlapping ownership therefore persists beyond the July 2006 section.

- **July 2003 reproduction, 2026-09-10:** `P-ARTALG-JU03-6` acquired a complete source-checked proof while this stream was rendering its missing diagram; it was read and retained. An exact-context patch for `P-ARTALG-JU03-9` was then rejected because another writer had inserted a source-check entry after the initial read. No part of that patch applied. Another `agents.status` request returned `WORKER_IDENTITY_LOST`, so no addressable owner could be reached through that tool. These are further same-range collisions, not conflicts with the disjoint UCSD or UGA edits elsewhere in the checkout.

- **Further reproduction, 2026-09-10:** a live source-order query returned `P-ARTALG-JU06-6` without a solution; the subsequent native read found a newly authored 157-line card, and Git reported that path as modified. This stream had not edited it and left the other writer's proof untouched. Later exact-context patches for `P-ARTALG-JU06-9` and `P-ARTALG-JU06-12` likewise failed after another writer added complete proofs between the read and patch; those proofs were independently checked and preserved, with no overwrite. A further native `agents.status` request returned `WORKER_IDENTITY_LOST`. The overlap therefore persists in the July 2006 section. `AGENTS.md` still says streams use separate worktrees (lines 648–650), as does `CONTRIBUTING.md` (lines 41–45), despite the current explicit direct-to-main assignment; align that guidance with the actual workflow when repairing ownership coordination.

- **Additional reproduction:** the next card `P-T4WCS` received two independently correct proofs and duplicate audit keys in `cc3b2e722`; `f5f68b2db` reconciles them after full comparison. A further pair of native `agents.status` attempts both returned `WORKER_IDENTITY_LOST`, so this stream could not obtain an addressable owner for coordination either.

- **Object and need:** direct-to-main authorship for the assigned interval `SRC-ALG-ART-HEACCB` through `SRC-TEXT-SMI`; each card must have one active writer so a completed proof can be reviewed and committed without overwriting another author's work.
- **Observed evidence:** on 2026-09-10, `P-I5GAL` was read as an unsolved card with no audit entries. Before the prepared patch was applied, another writer added an audit and a complete proof. The patch failed its exact-context check and changed nothing. A subsequent read showed the new proof, and Git then recorded it in `7a51eaba1`. The immediately following source-order card, `P-RK2VH`, also acquired an external edit while this stream had not touched it. This establishes actual overlap inside `SRC-ART-ALG-2003-2009-PRELIMS`, not merely unrelated changes elsewhere in the shared checkout; attribution of the two external edits to the same conversation was not established.
- **Impact and owner:** the stated file-disjointness assumption does not hold for this interval. Advancing both writers through the same ordered worklist risks repeated collisions and lost or duplicated proofs; the live card edits were preserved.
- **Uncertainty:** the other writer's identity and upstream assignment were not established. Two native worker-status requests returned `WORKER_IDENTITY_LOST`. A recording search for `P-I5GAL` returned only unattributed session buckets, so it supplied no addressable conversation owner.
- **Repair:** restore one active writer for this interval and working conversation identity for worker coordination, while retaining the already committed proofs and the current writer's uncommitted card. Do not resolve the collision by overwriting the live card or moving this stream outside its assigned range.

### A read-only connector command was rejected before execution

- **July 2013 check and inventory requests:** the combined `P-XVV4O` single-card check, whitespace check, and diff read was rejected before execution with the safety-status message. Separate `just check-card` and `just diff-card` requests succeeded, followed by a successful whitespace check and commit `0150fd7f8`. A later combined Git-status/complaint-diff request and read-only `Corpus`/`parse_cards` inventory request was also rejected before execution; the separate complaint diff and native `just unsolved-in` invocation were usable. These rejections do not establish failed repository checks.

- **Completion-query reproduction, 2026-09-10:** a read-only `Corpus`/`parse_cards` measurement of the two algebra packets was rejected before execution after the June 2015 proofs were committed. Separate calls to the existing `just unsolved-in` recipe remain the source-order measurement route; the rejected request supplies no evidence of a parser or corpus failure.

- **Commit-poll reproduction, 2026-09-10:** an empty-input `write_stdin` poll of the `P-ARTALG-AL04-9` commit session was rejected with the same safety-status message. A separate read-only Git check confirmed commit `c672be69b` and a clean card path. The rejection therefore obstructed reading the result; it did not mean the commit failed or repository access was unavailable.

- **Additional reproduction, 2026-09-10:** a batched read-only request for Git status/history, TODO text, and authoring-command discovery was rejected with the same safety-status message. Separate native file reads and a smaller Git-status command succeeded. No requested mutation or repository check was involved.

- **Object and need:** source-ordered authoring in the `SRC-ALG-ART-HEACCB` through `SRC-TEXT-SMI` range; reading a selected card, finding its retained source, and inspecting a Git diff should work without mutation.
- **Observed evidence:** on 2026-09-10 a combined `just read-card P-CSEAZ`, `find assets/attachments ...`, and `git diff -- COMPLAINTS.md` invocation was blocked with “we couldn't determine the safety status of the request.” Running the same read-only operations in separate calls succeeded. Later, two empty-input polls of the running `just read-card P-JH3BD` session received the same rejection; the native connector read succeeded for the card. The first image-view request for the rendered June 2008 Rings page was also rejected, while an identical retry displayed it successfully.
- **Impact and owner:** connector request screening interrupted source reading before any command ran. This is connector-owned, not a corpus validation failure.
- **Uncertainty:** the rejections did not identify an offending operation. Both a compound read-only command and empty-input session polling were affected; no causal distinction was supplied.
- **Repair:** expose the specific rejected operation and permit harmless read-only execution and polling. Alternate read calls restored source access but do not repair the screening defect.

### The required Zotero bibliography service is not listening

- **Object and need:** adding an external mathematical reference during `P-CSEAZ` solution authorship; `vocabularies/references.bib` is generated and `tools/sync_bibliography.py` requires the local Zotero/Better BibTeX service rather than hand-authored entries.
- **Observed evidence:** on 2026-09-10 `curl --max-time 5 http://127.0.0.1:23119/api/users/0/items?q=SmallGrp\&format=json\&limit=5` failed immediately with connection refused. Inspection of `tools/sync_bibliography.py` confirmed that its export endpoint uses the same host and port. Integration discovery returned no available Zotero connector.
- **Impact and owner:** new bibliography entries cannot be imported through the documented path while the desktop service is unavailable. Existing citations and independently proved mathematics remain usable; the generated bibliography was left unchanged.
- **Uncertainty:** this establishes local endpoint unavailability at the time of the request, not loss of the Zotero library or the absence of the work from that library.
- **Repair:** restore the documented Zotero/Better BibTeX export service, then add and export new references through that service.

### Primary local repository connector can silently become unavailable

- **Object and need:** local-repository work through the Chat On Steroids connector; repository reads and terminal commands should remain available while a scoped authoring stream is active.
- **Observed evidence:** on 2026-09-09, the first attempt to read `AGENTS.md`, `CONTRIBUTING.md`, git status, and git history failed before executing with `Tunnel-client has not been seen for 300 seconds. Ensure tunnel-client is running and connected.` The secondary local connector was available and executed the same commands successfully.
- **Impact and owner:** repository work is blocked when no secondary connector is available; with a secondary connector, the failure still adds avoidable recovery work and makes the primary connection state misleading. This is tooling/infrastructure-owned rather than corpus-owned.
- **Uncertainty:** verified for one primary-connector call in this session; the duration and root cause of the disconnect were not observable from the repository side.
- **Repair:** make connector liveness visible before invocation or transparently fail over to an available local connector, so repository reads do not fail solely because one tunnel has aged out.

### Commit history carries Claude session-provenance trailers

- **Object and need:** this repository's public git history; commit messages should carry no
  agent-session provenance URLs or trailers, per the same policy the fleet's other
  repositories state explicitly.
- **Observed evidence:** on 2026-09-10, `git log --all --grep='Claude-Session'` returns 172
  commits carrying a `Claude-Session: https://…` trailer, the earliest dated 2026-08-27.
  171 of them are reachable from `origin/main`, i.e. already published; exactly one is local
  and unpushed.
- **Impact and owner:** published history exposes session URLs indefinitely, and every future
  agent-authored commit will keep adding them until the commit path stops emitting the
  trailer. Two separable pieces of work: (a) stop new trailers at their source — whatever
  composes commit messages for agent sessions in this repo — and (b) decide the disposition of
  the 171 published commits, which can only be cleaned by rewriting published history and
  force-pushing, a repository-owner decision.
- **Uncertainty:** the emitting component was not identified from the repository side; the
  count is exact as of 2026-09-10.
- **Repair:** land (a) first so the count stops growing, then record an explicit decision on
  (b) rather than leaving published history in an unreviewed state.

### Concurrent branch consolidation reset a live worker's tree and lost authored work

- **Object and need:** branch consolidation in a shared checkout that live authoring sessions
  are working in; merging must never disturb another session's index or working tree.
- **Observed evidence:** on 2026-09-10 two consolidation runs executed concurrently. One used
  porcelain `git merge` with `git merge --abort` on conflict in the shared checkout; its abort
  reset the tree under a live worker, and commit `81373e972` records the recovery — "restore
  21 authored solutions lost from the shared worktree — 962 lines … existed only in the
  worktree and in no commit when the tree was reset under a live worker during branch
  consolidation." The concurrent run using `git merge-tree` + `git commit-tree` +
  compare-and-swap `git update-ref`, never touching the shared index, completed 20 merges
  across 44 branches with no such loss.
- **Impact and owner:** any future consolidation in this repository can repeat the loss. The
  work is only recoverable while it still exists in a worktree; nothing in the repository
  prevents the reset.
- **Uncertainty:** whether other authored files were lost and not noticed was not established;
  only the 21 files named in the rescue commit are confirmed.
- **Repair:** make the safe method the repository's documented consolidation procedure —
  compute merges out of tree, advance `main` by compare-and-swap ref update, sync only
  merge-changed paths, and skip any branch whose changed paths intersect the checkout's dirty
  set — and require a single consolidation owner at a time so two runs cannot race.

### `apply_patch` is unavailable in the repository shell

- **Object and need:** single-card authored edits in the local repository shell; a patch utility should support narrow, reviewable edits without rewriting unrelated content.
- **Observed evidence:** on 2026-09-10, invoking `apply_patch` from `/home/dzack/gitclones/new-qual-site` failed with `zsh:1: command not found: apply_patch` before changing `P-SP3SP`.
- **Impact and owner:** repository authoring must fall back to whole-file writes or lower-level text tools, increasing the chance of incidental edits. This is environment/tooling-owned, not corpus-owned.
- **Uncertainty:** only this shell environment was tested; `apply_patch` may exist in other harnesses.
- **Repair:** provide the patch helper consistently in repository shells, or document the supported narrow-edit command for this environment.

### `P-MFVEZ` omits the orientation of the square boundary

- **Object and need:** `P-MFVEZ` in `SRC-UGA-PRELIM-SPRING-2003`; a line integral around a closed curve requires an orientation, and Green's theorem uses the positive orientation convention.
- **Observed evidence:** both `assets/attachments/extracted/grad_prelim_Spring03.md` and the authored card say only that $C$ is the boundary of the unit square in the first quadrant. They do not state clockwise or counterclockwise orientation. Direct computation gives $1/2$ counterclockwise and $-1/2$ clockwise.
- **Impact and owner:** the source question has two possible numerical answers unless the usual positive-orientation convention is understood implicitly. The card solution now states both values and performs both requested computations for the positive orientation.
- **Uncertainty:** the original PDF may have conveyed an arrow graphically that the Markdown extraction lost; this was not established from the textual extraction.
- **Repair:** preserve the source wording, but retain the orientation caveat in the mathematical solution unless the original PDF is visually checked and an orientation mark is confirmed.

### `just unsolved-in` can hang indefinitely while scanning the corpus

- **Additional measurement, 2026-09-10:** `UV_NO_SYNC=1 just unsolved-in SRC-ALG-ART-HEACCB` produced no output for at least 46 seconds, then completed successfully with zero unsolved appearances. This run used `qualc.authoring`, not `tools/unsolved_queue.py`; it confirms a long delay, not an indefinite hang or a diagnosed deadlock.

- **Object and need:** `just unsolved-in <collection>` during source-ordered solution authoring; it should return the unsolved appearances for one collection promptly without regenerating `queues/C-unsolved-cards.md`.
- **Observed evidence:** on 2026-09-10, `just unsolved-in SRC-UGA-PRELIM-SPRING-2004` remained running for more than two minutes in `tools/unsolved_queue.py` without producing output; the invocation was terminated before any authored edit.
- **Impact and owner:** collection-by-collection solution work stalls on the repository's designated selection command. This is tooling-owned rather than mathematical-content-owned.
- **Uncertainty:** the host is under concurrent fleet load, so the delay may be performance-sensitive rather than a deterministic deadlock.
- **Repair:** make `unsolved-in` use the already-built catalog or otherwise bound the collection-scoped scan so one source lookup does not require an unbounded whole-corpus pass.

### Direct-to-`main` streams can globally block unrelated card commits with Git sequencer state

- **July 2013 reproduction:** the `just commit-card` attempt for `P-W13IN` returned exit 1 with `Cherry-pick currently in progress` and no pending change to that card. Immediate inspection found `f2c54e941` already committed on `main`, a clean card path, and no remaining `CHERRY_PICK_HEAD`. Thus this attempt raced with another stream's successful commit, rather than exposing a failed mathematical or schema check. No sequencer state was aborted or otherwise modified by this stream.

- **Object and need:** concurrent file-disjoint solution streams committing directly to `main`; one stream's commit operation should not prevent another stream from banking an unrelated card.
- **Observed evidence:** on 2026-09-10, `just commit-card P-S04DG` and later `just commit-card P-S05X3` each failed because the shared checkout was temporarily in `Cherry-pick currently in progress`, even though the concurrently edited card was in a disjoint collection. In both cases the intended prelim card later appeared as a clean committed path after the foreign sequencer operation completed.
- **Impact and owner:** Git sequencer state is checkout-global, so file-disjointness does not make direct-to-main porcelain operations independent; unrelated card commits can fail or be delayed despite no content-path collision.
- **Uncertainty:** the other stream's exact wrapper was not identified; the observed state was standard Git cherry-pick sequencer state in the shared checkout.
- **Repair:** use a commit path that constructs commits without checkout-global sequencer state, or serialize operations that invoke cherry-pick/rebase while preserving file-disjoint authorship on `main`.


### `P-OK5P3` has the wrong arc endpoint and resulting title

- **Object and need:** `P-OK5P3` in `SRC-UGA-PRELIM-SPRING-2007`; the card must reproduce the exam path before a line integral can be solved.
- **Observed evidence:** the preserved Spring 2007 exam extraction says the counterclockwise circle arc runs from `(2,0)` to `(0,2)`. The card instead said `(0,-2)`, and its title consequently described a three-quarter-circle path rather than the source's first-quadrant quarter-circle path.
- **Impact and owner:** the wrong endpoint changes the curve and therefore the line integral. The problem card owns the source-faithful correction.
- **Uncertainty:** none in the retained textual extraction; it explicitly names `(0,2)`.
- **Repair:** corrected the endpoint and title on `P-OK5P3` and solved the resulting positively oriented quarter-disk integral.
