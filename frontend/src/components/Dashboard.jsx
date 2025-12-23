import DonutChart from "./DonutChart";

export default function Dashboard({ data }) {
  return (
    <>
      <DonutChart title="Statut global documents" data={data.documents} />
      <DonutChart title="Par type de document" data={data.byType} />
      <DonutChart title="Par personne" data={data.byPerson} />
    </>
  );
}
