import { UserButton } from "@clerk/nextjs"


type Props = {}

const RootPage = (props: Props) => {
  return (
    <div>
     <UserButton afterSignOutUrl="/" />


    </div>
  )
}

export default RootPage