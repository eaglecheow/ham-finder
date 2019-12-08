import React from "react";
import logo from "./logo.svg";
import "./App.css";

import { IDocumentCardActivityPerson } from "office-ui-fabric-react/lib/DocumentCard";
import { TestImages } from "@uifabric/example-data";
import { IStackTokens, Stack } from "office-ui-fabric-react/lib/Stack";
import { AccidentCard } from "./components/AccidentCard";

const people: IDocumentCardActivityPerson[] = [
  { name: "Eagle Cheow", profileImageSrc: TestImages.personaMale },
  { name: "Yvette Tan", profileImageSrc: "", initials: "YT" },
  { name: "John Doe", profileImageSrc: TestImages.personaMale },
  { name: "Jane Doe", profileImageSrc: TestImages.personaFemale }
];

class AccidentDocumentCardList extends React.PureComponent {
  public render(): JSX.Element {
    const stackTokens: IStackTokens = { childrenGap: 20 };

    return (
      <Stack tokens={stackTokens}>
        <AccidentCard coordinate={[2.1, 101.22]} people={people[0]} />
        <AccidentCard coordinate={[2.2, 102.44]} people={people[3]} />
        <AccidentCard coordinate={[2.133, 101.33]} people={people[2]} />  
      </Stack>
    );
  }
}

const App: React.FC = () => {
  return (
    <React.Fragment>
      <AccidentDocumentCardList />
    </React.Fragment>
  );
};

export default App;
