def print_owing(invoice):
    print_banner()
    outstanding = calculate_outstanding()

    # print details

    print(f'name: {invoice.customer}')
    print(f'amount: {outstanding}')


def print_owing_refactor(invoice):
    print_banner()
    outstanding = calculate_outstanding()

    # print details
    def print_details():
        print(f'name: {invoice.customer}')
        print(f'amount: {outstanding}')

    print_details()


def print_owing(invoice):
    outstanding = 0

    print("***********************")
    print("**** Customer Owes ****")
    print("***********************")

    #  calculate outstanding
    for o in invoice.orders:
        outstanding += o.amount

    # record due date
    today = Clock.today
    from datetime import timedelta
    invoice.dueDate = today + timedelta(days=30)

    # print details
    print(f'name: {invoice.customer}')
    print(f'amount: {outstanding}')
    print(f'due: {invoice.dueDate.toLocaleDateString()}')


if __name__ == '__main__':
    """
    Docs:
        ```js
function printOwing(invoice) {
  printBanner();
  let outstanding = calculateOutstanding();

  //print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}

function printOwing(invoice) {
  printBanner();
  let outstanding = calculateOutstanding();
  printDetails(outstanding);

  function printDetails(outstanding) {
    console.log(`name: ${invoice.customer}`);
    console.log(`amount: ${outstanding}`);
  }
}
        ```
    """
    print_owing()
