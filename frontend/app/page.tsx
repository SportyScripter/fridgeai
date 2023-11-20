// `app/page.tsx` is the UI for the `/` URL
export default function Page() {
  return <div>
    <Komponent1>
      <Komponent2 text={"Props"}>
        Test 2
        <Komponent3 num={123} />
        </Komponent2>

        <Komponent2 text="test123">
          <Komponent3 num={123} />
          </Komponent2>
    </Komponent1>
  </div>
}

function Komponent1({children}: {children: React.ReactNode}) {
return <main>
  {children}
</main>
}

function Komponent2({children, text}: {children: React.ReactNode, text: string}) {
return <div>
  {text}
  
  <span>{children}</span>
</div>

}

function Komponent3({num}: {num?: number}) {
return <h3>{num}</h3>
}