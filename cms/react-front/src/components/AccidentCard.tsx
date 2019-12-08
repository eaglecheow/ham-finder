import React from "react";
import {
  IDocumentCardActivityPerson,
  DocumentCard,
  DocumentCardType,
  DocumentCardPreview,
  DocumentCardDetails,
  DocumentCardTitle,
  DocumentCardActivity
} from "office-ui-fabric-react/lib/DocumentCard";
import { TestImages } from "@uifabric/example-data";

export const AccidentCard: React.FC<{
  coordinate: number[];
  people: IDocumentCardActivityPerson;
}> = props => {
  const { coordinate, people } = props;

  return (
    <React.Fragment>
      <DocumentCard
        aria-label={`Accident card at coorinate: ${coordinate[0]}, ${coordinate[1]}`}
        type={DocumentCardType.compact}
        onClickHref="https://bing.com"
      >
        <DocumentCardPreview
          previewImages={[
            {
              name: "Revenue stream proposal fiscal year 2016 version02.pptx",
              linkProps: {
                href: "http://bing.com",
                target: "_blank"
              },
              previewImageSrc: TestImages.documentPreview,
              iconSrc: TestImages.iconPpt,
              width: 144
            }
          ]}
        />
        <DocumentCardDetails>
          <DocumentCardTitle
            title={`Help requested at [${coordinate[0]}, ${coordinate[1]}]`}
            shouldTruncate={true}
          />
          <DocumentCardActivity
            activity="Reported 5 mins ago"
            people={[people]}
          />
        </DocumentCardDetails>
      </DocumentCard>
    </React.Fragment>
  );
};
