const highlights = [
  ["$3.55M", "Savings delivered"],
  ["8+", "Years of experience"],
  ["800+", "NPI components sourced"],
  ["90%+", "Supplier OTIF achieved"],
];

const roles = [
  {
    date: "2023 - Present",
    company: "Alstom Transport · North America",
    title: "Buyer, NAM Region",
    copy: "Leading strategic sourcing for mechanical and structural commodities across North American rail programs—from RFQ and should-cost analysis to supplier selection, LTAs, risk mitigation, and executive reviews.",
    result: "$3.552M cost savings & avoidance",
  },
  {
    date: "2022",
    company: "Tesla · Fremont, California",
    title: "Global Supply Management Intern",
    copy: "Managed RFQs for manufacturing CAPEX and mechanical commodities, supporting supplier onboarding, bid evaluation, negotiations, NPI feasibility, and global supply continuity.",
    result: "High-impact CAPEX sourcing",
  },
  {
    date: "2019 - 2021",
    company: "Alstom Transport · India",
    title: "Supplier Coordinator",
    copy: "Led supplier development, localization, planning, and forecasting for manufacturing programs, partnering cross-functionally to unlock stronger delivery performance.",
    result: "4-week lead-time reduction",
  },
  {
    date: "2017 - 2019",
    company: "S.M. Auto & Autocomp · India",
    title: "Purchase Engineer / Executive",
    copy: "Built the foundation of a sourcing career through localization, JIT delivery, supplier development, inventory optimization, and production continuity.",
    result: "30% inventory cost reduction",
  },
];

const capabilities = [
  ["01", "Strategic Sourcing", "Commodity strategy, RFQ/RFP execution, global procurement, supplier selection, and long-term agreements."],
  ["02", "Cost & Commercial", "Should-cost modeling, bid analysis, contract negotiation, localization, and cost optimization."],
  ["03", "Supplier Performance", "Capability assessment, QCD improvement, Tier-1 relationships, risk mitigation, and supply continuity."],
  ["04", "Manufacturing Fluency", "Sheet metal, fabrication, stamping, welding, CNC machining, casting, molding, and surface finishing."],
];

export default function Home() {
  return (
    <main>
      <nav className="nav wrap" aria-label="Primary navigation">
        <a className="mark" href="#top" aria-label="Gautam Kumar home">GK<span>.</span></a>
        <div className="navlinks">
          <a href="#about">About</a><a href="#experience">Experience</a><a href="#expertise">Expertise</a>
        </div>
        <a className="navCta" href="mailto:vatsgr39@gmail.com">Let&apos;s connect <span>↗</span></a>
      </nav>

      <section className="hero wrap" id="top">
        <div className="heroCopy">
          <p className="eyebrow"><i /> Strategic sourcing & commodity management</p>
          <h1>Building resilient supply chains.<br/><em>Creating measurable value.</em></h1>
          <p className="intro">I&apos;m Gautam Kumar—a sourcing leader turning complex manufacturing challenges into stronger supplier partnerships, smarter commercial decisions, and lasting business impact.</p>
          <div className="heroActions">
            <a className="primary" href="#experience">Explore my work <span>↓</span></a>
            <a className="textLink" href="/Gautam-Kumar-Resume.pdf" target="_blank">View résumé <span>↗</span></a>
          </div>
        </div>
        <div className="portraitWrap">
          <div className="portrait"><img src="/gautam-kumar.jpeg" alt="Gautam Kumar in a grey suit" /></div>
          <div className="location"><span>Based in</span><b>United States</b></div>
          <div className="availability"><i /> Open to strategic opportunities</div>
        </div>
        <div className="scroll">SCROLL TO DISCOVER <span>↓</span></div>
      </section>

      <section className="metrics"><div className="wrap metricGrid">{highlights.map(([value,label])=><div key={label}><strong>{value}</strong><span>{label}</span></div>)}</div></section>

      <section className="about wrap section" id="about">
        <div><p className="sectionLabel">01 / Profile</p><h2>Where engineering rigor meets commercial strategy.</h2></div>
        <div className="aboutCopy"><p>Across rail, automotive, and advanced manufacturing, I&apos;ve built a career around one idea: the best sourcing decisions create value far beyond price.</p><p>My approach combines manufacturing fluency, data-led cost analysis, and trusted supplier relationships to improve quality, delivery, resilience, and total cost—at scale.</p><div className="degree"><span>Currently pursuing</span><b>Doctor of Business Administration</b><small>Business Administration & Quantitative Methods · Belhaven University</small></div></div>
      </section>

      <section className="experience section" id="experience">
        <div className="wrap"><p className="sectionLabel light">02 / Experience</p><div className="expHead"><h2>A track record of<br/><em>progress and impact.</em></h2><p>From the shop floor to global sourcing programs, each chapter has strengthened how I create value.</p></div>
          <div className="timeline">{roles.map((role,index)=><article key={role.company}><div className="index">0{index+1}</div><div className="date">{role.date}</div><div className="role"><small>{role.company}</small><h3>{role.title}</h3><p>{role.copy}</p><b>{role.result} <span>↗</span></b></div></article>)}</div>
        </div>
      </section>

      <section className="expertise wrap section" id="expertise">
        <p className="sectionLabel">03 / Expertise</p><div className="expertHead"><h2>Capabilities built for<br/><em>complexity.</em></h2><p>A practical blend of technical depth, commercial judgment, and cross-functional leadership.</p></div>
        <div className="capGrid">{capabilities.map(([n,title,copy])=><article key={n}><span>{n}</span><h3>{title}</h3><p>{copy}</p><b>↗</b></article>)}</div>
        <div className="tools"><span>TOOLS & METHODS</span><div>{["SAP MM","Ariba","Power BI","Advanced Excel","SQL","Tableau","Lean","Six Sigma"].map(x=><b key={x}>{x}</b>)}</div></div>
      </section>

      <section className="education section"><div className="wrap"><p className="sectionLabel">04 / Education</p><h2>Always learning.<br/><em>Always advancing.</em></h2><div className="eduGrid"><article><b>2026 - 2029</b><h3>Doctor of Business Administration</h3><p>Belhaven University</p></article><article><b>2021 - 2022</b><h3>M.S. Industrial Engineering</h3><p>University of Houston · GPA 3.6</p></article><article><b>2018 - 2020</b><h3>MBA, Manufacturing Management</h3><p>BITS Pilani · CGPA 8.75</p></article><article><b>2013 - 2017</b><h3>B.Tech. Mechanical Engineering</h3><p>Punjab Technical University · GPA 3.6</p></article></div></div></section>

      <footer><div className="wrap footerInner"><div><p>Have a challenge worth solving?</p><h2>Let&apos;s build what&apos;s next.</h2><a href="mailto:vatsgr39@gmail.com">vatsgr39@gmail.com <span>↗</span></a></div><div className="footerLinks"><a href="https://www.linkedin.com/in/gautam-vats" target="_blank" rel="noreferrer">LinkedIn ↗</a><a href="tel:+12817997121">+1 281 799 7121</a><a href="/Gautam-Kumar-Resume.pdf" target="_blank">Résumé ↗</a></div></div><div className="wrap copyright"><span>© 2026 Gautam Kumar</span><span>Strategic Sourcing · Supply Chain · Manufacturing</span></div></footer>
    </main>
  );
}
