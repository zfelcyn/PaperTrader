using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PaperTrader.Core.Models;

public enum OrderType { Buy, Sell }

public class Trade
{
    public Guid Id { get; set; } = Guid.NewGuid();
    public string Symbol { get; set; } = string.Empty;
    public OrderType OrderType { get; set; }
    public int Quantity { get; set; }
    public decimal Price { get; set; }
    public DateTime ExecutedAt { get; set; } = DateTime.UtcNow;
}
